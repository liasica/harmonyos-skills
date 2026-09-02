---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-19
title: 自动化测试框架如何读取应用内的文件
breadcrumb: FAQ > DevEco Studio > 应用测试 > 自动化测试框架如何读取应用内的文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:505c50d1df94f049c28cba4cf8767946eb20c65996fe27a42bc8a2fa49bc4f88
---

## 问题现象

使用自动化测试框架编写一些脚本模拟用户的行为，比如打开应用，点击某些页面，触发某些异常，然后需要将产生的结果数据与理想的结果的数据进行对比并校验。

结果数据存储在应用沙箱，如何读取这些数据？

## 背景知识

1. 基于Hypium的自动化测试框架指南：[应用UI测试（基于Python）](../harmonyos-guides/hypium-python-guidelines.md)。
2. 基于单元测试和UI测试的自动化测试框架指南：[自动化测试框架使用指导](../harmonyos-guides/arkxtest-guidelines.md)。

## 解决方案

假设要测试如下代码：

```ts
import { fileIo as fs, ReadOptions } from '@kit.CoreFileKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  hostContext = this.getUIContext().getHostContext();

  build() {
    Column() {
      Button('保存文件')
        .id('save')
        .onClick(async () => {
          await this.saveFile();
        })
    }
    .height('100%')
    .width('100%')
  }

  async saveFile() {
    const str = '测试数据';
    const file_path = this.hostContext?.cacheDir + '/test.txt';
    let file = fs.openSync(file_path, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    try {
      await fs.write(file.fd, str);
      let arrayBuffer = new ArrayBuffer(1024);
      let readOptions: ReadOptions = {
        offset: 0,
        length: arrayBuffer.byteLength
      };
      let readLen = await fs.read(file.fd, arrayBuffer, readOptions);
      let buf = buffer.from(arrayBuffer, 0, readLen);
      console.info('文件内容: ' + buf.toString());
    } catch {
      console.error('something wrong');
    } finally {
      fs.close(file);
    }

  }
}
```

* **方案1**：基于Hypium的自动化测试框架。

  通过driver.pull\_file将应用内的文件内容读取到PC侧，然后通过Python的with open()方法获取到file对象，即可比对数据。

  ```python
  from devicetest.core.test_case import TestCase, Step
  from hypium import UiDriver, BY

  class TC_001(TestCase):

      def __init__(self, controllers):
          self.TAG = self.__class__.__name__
          super().__init__(self.TAG, controllers)
          self.driver = UiDriver(self.device1)
          self.packageName = "com.huawei.myapplication"
          self.abilityName = "EntryAbility"

      def setup(self):
          Step('1.关闭应用')
          self.driver.stop_app(self.packageName)

      def process(self):
          Step('2.启动应用')
          self.driver.start_app(self.packageName, self.abilityName)

          Step('3.点击保存数据按钮')
          component = self.driver.find_component(BY.text('保存文件'))
          component.click()

          Step('4.获取应用缓存文件')  # 此处需要使用真实路径
          self.driver.pull_file(f"/data/app/el2/100/base/{self.packageName}/haps/entry/cache/test.txt", "test.txt")
          Step('5.读取本地文件')
          with open('test.txt', 'r', encoding='utf-8') as f:
              data = f.read()
              print(data)
              self.driver.log.info('文件数据: ' + data)
  ```
* **方案2**：基于UITest的自动化测试。

  通过[fs.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)读取应用文件后通过expect()断言比对数据。

  ```ts
  import { describe, it, expect } from '@ohos/hypium';
  // 导入测试依赖kit
  import { abilityDelegatorRegistry, Driver, ON } from '@kit.TestKit';
  import { UIAbility, Want } from '@kit.AbilityKit';
  import {fileIo as fs, ReadOptions } from '@kit.CoreFileKit'
  import { buffer } from '@kit.ArkTS';

  const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator()
  const bundleName = abilityDelegatorRegistry.getArguments().bundleName;
  function sleep(time: number) {
    return new Promise<void>((resolve: Function) => setTimeout(resolve, time));
  }

  export default function abilityTest() {
    describe('IndexTextTest', () => {
      // UI测试
      it('testUiExample',0, async (done: Function) => {
        console.info("uitest: TestUiExample begin");
        //start tested ability
        const want: Want = {
          bundleName: bundleName,
          abilityName: 'EntryAbility'
        }
        await delegator.startAbility(want);
        await sleep(1000);
        //check top display ability
        const ability: UIAbility = await delegator.getCurrentTopAbility();
        console.info("get top ability");
        expect(ability.context.abilityInfo.name).assertEqual('EntryAbility');
        //init driver
        const driver = Driver.create();

        // 读取应用缓存目录下的文件
        const save_file_btn = await driver.findComponent(ON.id('save'));
        await save_file_btn.click();
        await driver.delayMs(1000);
        const file_path = ability.context.cacheDir + '/test.txt'
        let file = fs.openSync(file_path,fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE)
        try {
          let arrayBuffer = new ArrayBuffer(1024)
          let readOptions: ReadOptions = {
            offset: 0,
            length: arrayBuffer.byteLength
          }
          let readLen = await fs.read(file.fd, arrayBuffer, readOptions)
          let buf = buffer.from(arrayBuffer, 0 ,readLen)
          // 断言数据
          console.info(buf.toString())
          expect(buf.toString()).assertEqual('测试数据')
        } catch {
          console.error('something wrong')
        } finally {
          fs.close(file)
        }
        done();
      })
    })
  }
  ```
