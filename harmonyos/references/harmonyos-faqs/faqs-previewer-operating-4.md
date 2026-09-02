---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-4
title: 预览告警“There are properties not initialized”
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览告警“There are properties not initialized”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:becc6bf1c9502633e39bb02d45dbba9c2445d23e936d6c28844c83b808c29743
---

**问题现象**

启动预览后，预览窗口白屏，并显示错误信息：“Preview failed. View details in the PreviewerLog window.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/DYza_-BcQjyZX9G5Qq7KWg/zh-cn_image_0000002654837767.png "点击放大")

此时下方PreviewLog窗口出现告警信息：“There are properties not initialized.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/sCTJ7k5BTxe8OlwLsY0K8w/zh-cn_image_0000002624478456.png)

**解决措施**

预览页面或组件中存在未初始化成功的成员变量，调用这些成员变量的属性或方法时会导致错误，预览界面显示空白。导致该问题的常见原因包括：

场景一：使用AppStorage等方法设置全局变量。

场景二：使用router.getParams()获取路由参数。

使用自定义的Mock。

1. 在 oh-package.json5 中添加以下依赖。

   ```json
   "dependencies": {
     // The version number needs to be modified according to the relationship between hvigor and the SDK
     "@ohos/hamock": "1.0.0"
   }
   ```
2. 预览页面中导入mock依赖。

   ```typescript
   import { MockSetup } from '@ohos/hamock';
   ```
3. 设置mock数据。

   ```typescript
   @MockSetup
   mock(){
     this.fruit = new Fruit("apple");
   }
   ```

场景一：使用AppStorage等方法设置的全局变量，修改后的示例代码如下：

```typescript
import { MockSetup } from '@ohos/hamock';

export default class Fruit{
  public name: string;

  getName(): string{
    return this.name;
  }

  constructor(name: string) {
    this.name = name;
  }

}

@Entry
@Component
struct GlobalData {
  @State fruit:Fruit = AppStorage.get("fruit") as Fruit;

  @MockSetup
  mock(){
    this.fruit = new Fruit("apple");
  }

  build() {
    Row() {
      Column() {
        Text(this.fruit.name)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

场景二：使用路由参数，修改后的示例代码如下：

```typescript
import { MockSetup } from '@ohos/hamock';

@Entry
@Component
struct Page {
  @State params: object = this.getUIContext().getRouter().getParams();

  @MockSetup
  mock(){
    this.params = [];
    this.params["path"] = "path";
  }

  build() {
    Row() {
      Column() {
        Text(this.params['path'])
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
