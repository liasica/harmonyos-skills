---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-intelligentfilling-amend
title: 动态修改ContentType值
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 动态修改ContentType值
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:96dc8f7a1deb5f3644bf3559ba84e022284ae5b0bffb28f33dc7f61f705a5961
---

在填写实名信息表单的场景，表单中存在身份证和其他证件输入，其中，多种证件号共用一个输入框，ContentType.ID\_CARD\_NUMBER目前只支持身份证号的推荐、填充，不支持其他类型的证件，需要开发者根据输入场景动态配置输入框的ContentType，只在身份证输入场景下使用ContentType.ID\_CARD\_NUMBER。

## 效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/iLDkZtNTSviwSnt3ZEIX4Q/zh-cn_image_0000002706675246.png)

## 示例代码

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { autoFillManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SmartFill {
  // 与证件号码类型对应的ContentType。在此情况下，默认将ContentType设置为身份证号码对应的类型值。
  @State type: ContentType | undefined = ContentType.ID_CARD_NUMBER;
  @State isClicked: boolean = false;

  build() {
// ...
      Column({ space: 5 }) {
        Row() {
          Text('证件类型：').textAlign(TextAlign.End).width('25%')
          Select([{ value: '身份证' }, { value: '港澳通行证' }])
            .width('75%')
            .selected(0)
            .value('身份证')
            .onSelect((index: number, value: string) => {
              // 当用户选择ID类型时，更改与证件号码输入组件对应的ContentType值。
              hilog.info(0x0000, 'testTag', 'Select item changed, value: ' + value + ', index: ' + index);
              if (value === '身份证') {
                this.type = ContentType.ID_CARD_NUMBER;
              } else if (value === '港澳通行证') {
                this.type = undefined;
              }
              hilog.info(0x0000, 'testTag', 'ContentType changed, current type: ' + this.type);
            })
        }

        Row() {
          Text('姓名：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME)
        }

        Row() {
          Text('手机号码：').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(ContentType.PHONE_NUMBER)
        }

        Row() {
          Text('证件号码').textAlign(TextAlign.End).width('25%')
          TextInput().width('75%').contentType(this.type)
        }

        Button('保存')
          .onClick(() => {
            if (!this.isClicked) {
              // 主动触发保存历史表单输入。
              try {
                autoFillManager.requestAutoSave(this.getUIContext())
              } catch (err) {
                let e: BusinessError = err as BusinessError;
                hilog.error(0x0000, 'testTag', 'error: %{public}d %{public}s', e.code, e.message);
              }
              this.isClicked = true;
              // 设置超时时间以防止重复点击按钮保存历史表单输入。
              setTimeout(() => {
                this.isClicked = false;
              }, 1000)
              // 或者通过路由跳转其他页面触发保存历史表单输入。
              this.getUIContext().getRouter().pushUrl({
                url: 'xxx'
              })
            }
          })
          .width('50%')
      }
      .alignItems(HorizontalAlign.Center)
      .height('100%')
      .width('100%')
// ...
  }
}
```
