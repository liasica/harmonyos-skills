---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-693
title: 实现子组件创建和销毁后的排序显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现子组件创建和销毁后的排序显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4f5e714973cf791967baa073a7f5c3f5dd09898c91cdf7b68fc8abb533fe5cae
---

## 问题现象

视频会议场景下，邀请的成员中有人挂断或者超时未接听后，将其显示在已入会人员区域最后，当成员重新进入后，将其显示到已接听人员最后，如果有人点击离开会议，则将其显示在下方为未入会人员区域。效果如下图所示，如何实现这种排序显示效果？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/grsv_-gUTZKGcsc5n_tspQ/zh-cn_image_0000002628554752.png "点击放大")

## 背景知识

* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)：基于数组类型数据来进行循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。
* [findIndex](../harmonyos-references/arkts-apis-arkts-collections-array.md#findindex)：返回Array中第一个满足指定测试函数的元素的索引，如果所有元素都不满足，则返回-1。
* [splice](../harmonyos-references/arkts-apis-arkts-collections-array.md#splice-1)：删除Array中指定位置的元素，需要时在Array的指定位置插入新元素。
* [push](../harmonyos-references/arkts-apis-arkts-collections-array.md#push)：在ArkTS Array的末尾添加元素，并返回新的Array长度。

## 解决方案

可以自定义信息列表infoList维护成员的信息以及入会状态。详细如下：

1. 使用ForEach循环渲染，当有成员挂断时，修改该成员的信息Info，修改selected信息，重新排序显示在已入会人员区域。当有成员离开会议时，修改该成员的信息Info，修改flag信息，将其显示在未入会人员区域。
2. 当有新成员进入会议时，修改该成员的信息Info，修改selected信息，重新排序显示在已入会人员区域。

```ts
@Observed
class Info {
  @Track num: number = 0;
  @Track flag: boolean = true; // true:已入会(在上面),false:未入会(在下面)
  @Track selected: boolean = false; // 是否被选中
  @Track status: string = '接听'; // '接听'或'挂断'

  constructor(num: number, flag: boolean, selected: boolean = false, status: string = '接听') {
    this.num = num;
    this.flag = flag;
    this.selected = selected;
    this.status = status;
  }
}

// 按钮状态接口
interface ButtonState {
  joinEnabled: boolean; // 进入会议按钮是否可用
  hangUpEnabled: boolean; // 挂断按钮是否可用
  leaveEnabled: boolean; // 离开会议按钮是否可用
  joinColor: string; //进入会议按钮颜色
  hangUpColor: string; // 挂断按钮颜色
  leaveColor: string; // 离开会议按钮颜色
}

@Entry
@Component
struct sortExample {
  @State infoList: Info[] = [
    new Info(3, true, false, '接听'),
    new Info(5, true, false, '接听'),
    new Info(7, true, false, '接听'),
    new Info(9, true, false, '接听'),
    new Info(2, true, false, '接听')
  ];
  scroller: Scroller = new Scroller();
  scroller2: Scroller = new Scroller();

  // 获取当前选中的卡片
  getSelectedItem(): Info | undefined {
    return this.infoList.find(item => item.selected === true);
  }

  // 获取已入会人员（flag为true）- 按接听在前、挂断在后排序
  getJoinedMembers(): Info[] {
    const joined = this.infoList.filter(item => item.flag === true);
    // 排序：接听的在前，挂断的在后
    return [...joined.filter(item => item.status === '接听'), ...joined.filter(item => item.status === '挂断')];
  }

  // 获取未入会人员（flag为false）
  getUnjoinedMembers(): Info[] {
    return this.infoList.filter(item => item.flag === false);
  }

  // 清除所有选中状态
  clearAllSelected() {
    this.infoList.forEach(item => {
      item.selected = false;
    });
  }

  // 处理卡片点击
  onCardClick(item: Info) {
    this.clearAllSelected();
    item.selected = true;
    // 强制刷新UI
    this.infoList = [...this.infoList];
  }

  // 挂断：将选中的已入会接听成员改为挂断状态，并放到已入会最后面
  hangUpMeeting() {
    const selectedItem = this.getSelectedItem();
    if (!selectedItem || !selectedItem.flag || selectedItem.status !== '接听') {
      return;
    }

    selectedItem.status = '挂断'; // 改为挂断
    selectedItem.selected = false; // 清除选中

    // 重新排序：已入会按接听在前、挂断在后排序，未入会放到后面
    const joined = this.infoList.filter(item => item.flag === true);
    const joinedAnswered = joined.filter(item => item.status === '接听');
    const joinedHangUp = joined.filter(item => item.status === '挂断');
    const unjoined = this.infoList.filter(item => item.flag === false);
    this.infoList = [...joinedAnswered, ...joinedHangUp, ...unjoined];
  }

  // 离开会议：将选中的已入会人员移动到未入会区域末尾
  leaveMeeting() {
    const selectedItem = this.getSelectedItem();
    if (!selectedItem || !selectedItem.flag) {
      return;
    }

    selectedItem.flag = false; // 改为未入会
    selectedItem.selected = false; // 清除选中
    selectedItem.status = '接听'; // 重置为接听状态

    // 重新排序：已入会按接听在前、挂断在后排序，未入会放到后面
    const joined = this.infoList.filter(item => item.flag === true);
    const joinedAnswered = joined.filter(item => item.status === '接听');
    const joinedHangUp = joined.filter(item => item.status === '挂断');
    const unjoined = this.infoList.filter(item => item.flag === false);
    this.infoList = [...joinedAnswered, ...joinedHangUp, ...unjoined];
  }

  // 进入会议：将选中的未入会人员或挂断状态的已入会人员变为接听状态
  joinMeeting() {
    const selectedItem = this.getSelectedItem();
    if (!selectedItem) {
      return;
    }

    // 情况1：未入会人员
    if (!selectedItem.flag) {
      selectedItem.flag = true; // 改为已入会
      selectedItem.status = '接听'; // 设置为接听状态
    } else if (selectedItem.flag && selectedItem.status === '挂断') { // 情况2：已入会挂断状态
      selectedItem.status = '接听'; // 改为接听状态
    } else {
      return; // 其他情况无效
    }

    selectedItem.selected = false; // 清除选中

    // 重新排序：已入会按接听在前、挂断在后排序，未入会放到后面
    const joined = this.infoList.filter(item => item.flag === true);
    const joinedAnswered = joined.filter(item => item.status === '接听');
    const joinedHangUp = joined.filter(item => item.status === '挂断');
    const unjoined = this.infoList.filter(item => item.flag === false);
    this.infoList = [...joinedAnswered, ...joinedHangUp, ...unjoined];
  }

  // 按钮状态控制
  getButtonState() {
    const selectedItem = this.getSelectedItem();
    const state: ButtonState = {
      joinEnabled: false,
      hangUpEnabled: false,
      leaveEnabled: false,
      joinColor: '#CCCCCC',
      hangUpColor: '#CCCCCC',
      leaveColor: '#CCCCCC'
    };

    if (!selectedItem) {
      return state;
    }

    // 情况1：选中挂断状态的已入会卡片 或 未入会卡片 - 进入会议可用
    if ((selectedItem.flag && selectedItem.status === '挂断') || !selectedItem.flag) {
      state.joinEnabled = true;
      state.joinColor = '#0A59F7';
    }

    // 情况2：选中已入会且为接听的卡片 - 挂断和离开会议可用
    if (selectedItem.flag && selectedItem.status === '接听') {
      state.hangUpEnabled = true;
      state.leaveEnabled = true;
      state.hangUpColor = '#FF4D4F';
      state.leaveColor = '#FF4D4F';
    }

    // 情况3：选中已入会且为挂断的卡片 - 离开会议可用
    if (selectedItem.flag && selectedItem.status === '挂断') {
      state.leaveEnabled = true;
      state.leaveColor = '#FF4D4F';
    }

    return state;
  }

  @Builder
  infoCard(info: Info) {
    Column() {
      Text(info.num + '')
        .fontSize(24)
        .fontColor('#000000')

      if (info.flag === true) {
        // 只在已入会区域显示状态标签
        Text(info.status)
          .fontSize(12)
          .fontColor(info.status === '接听' ? '#0A59F7' : '#999999')
          .margin({ top: 4 })
      }
    }
    .width(75)
    .height(info.flag === true ? 95 : 75) // 已入会卡片更高，因为要显示状态文字
    .backgroundColor(info.flag === true ? (info.status === '接听' ? '#FFFFFF' : '#F5F5F5') : '#FFFFFF')
    .justifyContent(FlexAlign.Center)
    .border({
      width: info.selected ? 2 : 1,
      color: info.selected ? '#0A59F7' : '#E5E5E5',
      style: BorderStyle.Solid
    })
    .borderRadius(8)
    .onClick(() => {
      this.onCardClick(info);
    })
  }

  build() {
    Column({ space: 20 }) {
      // 1. 已入会人员区域 - 带淡色边框背景
      Text('已入会人员')
        .fontSize(18)
        .fontWeight(FontWeight.Bold)
        .width('100%')
        .textAlign(TextAlign.Start)

      List({ scroller: this.scroller, initialIndex: 0, space: 10 }) {
        ForEach(this.getJoinedMembers(),
          (item: Info) => {
            ListItem() {
              this.infoCard(item);
            }
          },
          (item: Info) => item.num.toString() + '_' + (item.flag ? '1' : '0') + '_' + (item.selected ? '1' : '0') +
            '_' + item.status
        )
      }
      .listDirection(Axis.Horizontal)
      .height(125)
      .width('100%')
      .padding(12)
      .backgroundColor('#F9F9F9')
      .borderRadius(12)
      .border({
        width: 1,
        color: '#E0E0E0',
        style: BorderStyle.Solid
      })
      .alignListItem(ListItemAlign.Start)

      // 2. 按钮区域 - 三个按钮在同一行完整显示
      Row({ space: 10 }) {
        Button('进入会议')
          .width(100)
          .height(40)
          .backgroundColor(this.getButtonState().joinColor)
          .enabled(this.getButtonState().joinEnabled)
          .onClick(() => {
            this.joinMeeting();
          })

        Button('挂断')
          .width(100)
          .height(40)
          .backgroundColor(this.getButtonState().hangUpColor)
          .enabled(this.getButtonState().hangUpEnabled)
          .onClick(() => {
            this.hangUpMeeting();
          })

        Button('离开会议')
          .width(100)
          .height(40)
          .backgroundColor(this.getButtonState().leaveColor)
          .enabled(this.getButtonState().leaveEnabled)
          .onClick(() => {
            this.leaveMeeting();
          })
      }
      .width('100%')
      .justifyContent(FlexAlign.SpaceBetween)
      .margin({ top: 10, bottom: 10 })

      // 3. 操作说明
      Column({ space: 5 }) {
        Text('操作说明：')
          .fontSize(16)
          .fontWeight(FontWeight.Bold)
        Text('1. 选中未入会卡片 → 仅“进入会议”可用（蓝色），移至上方接听状态')
          .fontSize(14)
          .fontColor('#666666')
        Text('2. 选中接听卡片 → “挂断”（红色）和“离开会议”（红色）可用')
          .fontSize(14)
          .fontColor('#666666')
        Text('3. 选中挂断卡片 → “进入会议”（蓝色）和“离开会议”（红色）可用')
          .fontSize(14)
          .fontColor('#666666')
        Text('4. 挂断卡片点击“进入会议”会重新变为接听状态')
          .fontSize(14)
          .fontColor('#666666')
        Text('5. 选中的人员卡片边缘会显示蓝色边框')
          .fontSize(14)
          .fontColor('#666666')
      }
      .alignItems(HorizontalAlign.Start)
      .width('100%')
      .padding(12)
      .backgroundColor('#F8F9FA')
      .borderRadius(8)
      .border({
        width: 1,
        color: '#E8E8E8',
        style: BorderStyle.Solid
      })

      // 4. 未入会人员区域 - 带淡色边框背景
      Text('未入会人员')
        .fontSize(18)
        .fontWeight(FontWeight.Bold)
        .width('100%')
        .textAlign(TextAlign.Start)
        .margin({ top: 10 })

      List({ scroller: this.scroller2, initialIndex: 0, space: 10 }) {
        ForEach(this.getUnjoinedMembers(),
          (item: Info) => {
            ListItem() {
              this.infoCard(item);
            }
          },
          (item: Info) => item.num.toString() + '_' + (item.flag ? '1' : '0') + '_' + (item.selected ? '1' : '0')
        )
      }
      .listDirection(Axis.Horizontal)
      .height(105)
      .width('100%')
      .padding(12)
      .backgroundColor('#F5F9FF')
      .borderRadius(12)
      .border({
        width: 1,
        color: '#D9E6F2',
        style: BorderStyle.Solid
      })
      .alignListItem(ListItemAlign.Start)
    }
    .width('100%')
    .height('100%')
    .padding(16)
  }
}
```
