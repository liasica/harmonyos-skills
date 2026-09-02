---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-monitorcrownevents
title: 旋转表冠事件监听
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 全局接口 > 旋转表冠事件监听
category: harmonyos-references
scraped_at: 2026-09-02T15:01:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f0395ce262b04325909a8f2494ff385cf20e95901c0d832b21de9fb3f2003954
---

本模块提供为当前页面设置旋转表冠事件监听器的能力，支持注册页面级的旋转表冠事件监听器，适用于需要在页面级统一监听旋转表冠操作并控制事件分发的场景。仅支持配备旋转表冠的设备。

**说明** 

本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## setMonitorForCrownEvents

setMonitorForCrownEvents(handler: Function): void

为当前页面设置旋转表冠事件监听器，当旋转表冠事件触发时，监听器会触发回调。

该监听器在发生[页面路由](js-apis-router.md)时将自动移除，使用[clearMonitorForCrownEvents()](js-components-common-monitorcrownevents.md#clearmonitorforcrownevents)接口可手动移除。

**说明** 

* 当发生页面路由时，监听器将自动移除，因此建议在页面的onShow[生命周期](../harmonyos-guides/js-framework-lifecycle.md)回调中调用此接口。
* 每个页面仅支持设置一个监听器，新注册的监听器会覆盖之前的监听器，系统将使用最后一次调用此接口时传入的监听器。
* 请勿在[app.js](../harmonyos-guides/js-framework-js-file.md)中使用此函数，其行为未定义。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Function | 是 | 旋转表冠事件发生后执行该回调。回调格式为(event)=>{ return false/true; }。  返回true时，旋转表冠事件不再分发给获焦的组件。  返回false时，旋转表冠事件会继续分发给获焦组件。当回调返回undefined或无返回值时，默认取值为false。  可通过入参获取旋转表冠事件信息，事件信息请参见**表1 CrownEvent对象属性列表**。 |

**表1** CrownEvent对象属性列表

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳，表示事件发生时距系统启动运行至今的时间。  单位：ms。 |
| angularVelocity | number | 否 | 否 | 旋转角速度，表示每秒旋转的角度。  逆时针旋转表冠时旋转角速度为正数，顺时针旋转表冠时旋转角速度为负数。  单位：°/s |
| degree | number | 否 | 否 | 相对旋转角度。  逆时针旋转表冠时相对旋转角度为正数，顺时针旋转表冠时相对旋转角度为负数。  单位：度。  取值范围：[-360, 360] |

## clearMonitorForCrownEvents

clearMonitorForCrownEvents(): void

清除当前页面的旋转表冠事件监听器，适用于页面不再需要监听旋转表冠事件，或需要恢复获焦组件默认响应旋转表冠事件的场景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在FA模型下使用。

## 示例

### 示例1（设置旋转表冠事件监听器）

该示例介绍如何通过[setMonitorForCrownEvents](js-components-common-monitorcrownevents.md#setmonitorforcrownevents)为页面设置旋转表冠事件监听器，并通过监听器的回调返回值控制List组件是否响应旋转表冠事件。

从API version 24开始，新增[setMonitorForCrownEvents](js-components-common-monitorcrownevents.md#setmonitorforcrownevents)接口和[clearMonitorForCrownEvents](js-components-common-monitorcrownevents.md#clearmonitorforcrownevents)接口。

```css
/* xxx.css */
.container {
    flex-direction: column;
    width: 100%;
    margin-top: 10px;
    align-items: center;
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: 500;
    margin-left: 12px;
}

.text {
    font-size: 50px;
    font-weight: 500;
    margin-left: 200px;
}
.listItem {
    width: 100%;
    height: 100px;
    line-height: 60px;
    border-bottom: 1px solid #DEDEDE;
    font-size: 20px;
}
.btn{
    width: 380px;
    height: 100px;
    font-size: 36px;
    margin: 10px;
}
```

```html
<!-- xxx.hml -->
<div class="container">
    <text class="title">
        {{ title }}
    </text>
    <button class="btn" type="capsule" value="clearMonitor" onclick="clearMonitor"></button>
    <button class="btn" type="capsule" value="flagChange" onclick="flagChange"></button>
    <list class="list" focusable="true" scrollpage="true">
        <list-item for="{{ array }}" class="listItem">
            <text class="text" onclick="toggleShow" show="{{ visible }}">{{ $item.value }}</text>
        </list-item>
    </list>
</div>
```

```js
// xxx.js
export default {
    data: {
        title: 'TestPage',
        count: 0,
        display: true,
        array: [
            { 'value': 'TestListItem0' },
            { 'value': 'TestListItem1' },
            { 'value': 'TestListItem2' },
            { 'value': 'TestListItem3' },
            { 'value': 'TestListItem4' },
            { 'value': 'TestListItem5' },
            { 'value': 'TestListItem6' },
            { 'value': 'TestListItem7' },
            { 'value': 'TestListItem8' },
            { 'value': 'TestListItem9' },
        ],
        flag: false
    },
    onShow() {
        setMonitorForCrownEvents((event) => {
            console.info('event timestamp is: ', event.timeStamp, ', angularVelocity is: ',
                event.angularVelocity);
            console.info('rotate is: ', event.rotate);
            return this.flag;
        });
    },
    flagChange() {
        this.flag = !this.flag;
    },
    clearMonitor() {
        clearMonitorForCrownEvents();
    }
}
```
