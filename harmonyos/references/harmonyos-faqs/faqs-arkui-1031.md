---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1031
title: 分类筛选功能异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 分类筛选功能异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6c79e16a83f40c1264461e796dd3a313e9e86faea81c5d7fb5add57d9955ab97
---

## 问题现象

点击打开筛选界面，有分类和主题两个部分，主题可以多选，若没有选择主题，则分类只能选择一个。但是选择主题后，多选分类，此时再将选择的主题全部取消，分类还是会保存多选状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/lFm-Mq4ITXaMPRVuT484AQ/zh-cn_image_0000002658924029.png "点击放大")

## 背景知识

[模态转场](../harmonyos-guides/arkts-modal-transition.md)是新的界面覆盖在旧的界面上，旧的界面不消失的一种转场方式，常用于实现筛选框、侧边栏等功能。

## 问题定位

1. 使用DevEco Testing中的UIViewer工具，查看筛选界面的布局，发现筛选界面使用[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)实现，内容使用[线性布局](../harmonyos-guides/arkts-layout-development-linear.md)以及[Grid组件](../harmonyos-references/ts-container-grid.md)实现，不涉及与H5页面的交互。
2. 根据问题现象，推测在取消全部主题的场景中未重置分类。
3. 排查代码，查看是否有单独记录分类和主题两个内容的选择状态，并在主题选择为空时将分类的选择也重置。

## 分析结论

当主题的选择内容从有变无时，未对分类选项做重置操作，导致取消主题的所有选择后，分类仍为多选状态。

## 修改建议

在点击主题选项时添加判断，若主题选择为空并且分类为多项状态，则将筛选重置，示例代码如下：

```ets
import { PromptAction, UIContext } from '@kit.ArkUI';
@ObservedV2
  // 观察点击事件
class textFont { // 创建一个文本类
  tex: number = 0;
  @Trace isClick: boolean = false; // 记录是否被点击

  constructor(tex: number) {
    this.tex = tex; // 初始化文本值
  }
}

@Entry
@Component
struct BindSheetSelect {
  @State isShowSheet: boolean = false; // 控制筛选框显隐
  selectList: Array<textFont> = []; // 分类列表
  themeList: Array<textFont> = []; // 主题列表
  @State selectNum: number = 0; // 选择的分类数量
  @State themeNum: number = 0; // 选择的主题数量
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();

  aboutToAppear(): void {
    for (let i = 0; i < 4; i++) { // 初始化列表
      this.selectList.push(new textFont(i));
      this.themeList.push(new textFont(i));
    }
  }

  @Builder
  SheetBuilder() {
    Column() {
      Column({ space: 30 }) {
        Row() {
          Text('分类')
        }
        .width('100%')
        .justifyContent(FlexAlign.Start)
        .padding({
          left: 30
        })

        Grid() {
          ForEach(this.selectList, (item: textFont) => {
            GridItem() {
              Row() {
                Text(item.tex.toString())
                  .fontColor('#0A59F7')
              }
              .backgroundColor('#0d000000')
              .borderWidth(item.isClick ? 1 : 0)
              .borderColor('#0A59F7')
              .opacity(item.isClick ? 1 : (this.selectNum ? (this.themeNum ? 1 : 0.4) : 1))
              .borderRadius(20)
              .width(100)
              .height(30)
              .justifyContent(FlexAlign.Center)
            }
            .onClick(() => { // 切换点击状态
              if (!item.isClick) { // 若没有被点亮
                if (!this.selectNum) { // 没有选择过分类，可以选一个
                  item.isClick = true;
                  this.selectNum++;
                } else {
                  if (this.themeNum) { // 选了主题，可以多选分类
                    item.isClick = true;
                    this.selectNum++;
                  }
                }
              } else { // 若被点亮了,则取消点亮状态
                item.isClick = false;
                this.selectNum--;
              }
            })
          })
        }
        .width('100%')
        .height(80)
        .columnsTemplate('1fr 1fr 1fr')
        .rowsGap(20)

        Row() {
          Text('主题')
        }
        .width('100%')
        .justifyContent(FlexAlign.Start)
        .padding({
          left: 30
        })

        Grid() { // 使用网格容器选项列表
          ForEach(this.themeList, (item: textFont) => {
            GridItem() {
              Row() {
                Text(item.tex.toString()) // 选项内容
                  .fontColor('#0A59F7')
              }
              .backgroundColor('#0d000000')
              .borderWidth(item.isClick ? 1 : 0)
              .borderColor('#0A59F7')
              .borderRadius(20)
              .width(100)
              .height(30)
              .justifyContent(FlexAlign.Center)
            }
            .onClick(() => {
              if (item.isClick) { // 判断选项是否被点击
                item.isClick = !item.isClick;
                this.themeNum--; // 主题选择数量
                if (this.themeNum === 0 && this.selectNum > 1) { // 当主题选项为空，且分类为多选，则将所有选项全部重置
                  this.selectNum = 0; // 清空分类选项
                  for (let i = 0; i < 4; i++) { // 重置所有内容
                    this.selectList[i].isClick = false;
                    this.themeList[i].isClick = false;
                  }
                }
              } else {
                item.isClick = !item.isClick;
                this.themeNum++;
              }

            })
          })
        }
        .width('100%')
        .height(80)
        .columnsTemplate('1fr 1fr 1fr')
        .rowsGap(20)

        Row() {
          Button('确定')
            .onClick(() => {
              if (!this.selectNum) {
                this.promptAction.openToast({
                  message: '未选分类'
                });
              } else if (!this.themeNum) {
                this.promptAction.openToast({
                  message: '未选主题'
                });
              } else {
                this.isShowSheet = false;
              }
            })

          Button('取消')
            .onClick(() => {
              this.isShowSheet = false;
            })
        }
        .width('100%')
        .height('15%')
        .justifyContent(FlexAlign.SpaceEvenly)
      }
    }
    .width('100%')
    .height('100%')
  }

  @Builder
  titleBuilder() {
    Column() {
      Text('筛选')
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }

  build() {
    Column() {
      Button('点击打开筛选框')
        .onClick(() => {
          this.isShowSheet = !this.isShowSheet;
        })
        .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
          detents: [SheetSize.MEDIUM, SheetSize.LARGE, 600],
          preferType: SheetType.BOTTOM,
          title: this.titleBuilder(),
          showClose: false,
          dragBar: false,
          backgroundColor: Color.White
        })
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
