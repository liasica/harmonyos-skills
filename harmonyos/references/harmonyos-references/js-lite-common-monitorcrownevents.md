---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-monitorcrownevents
title: 旋转表冠事件监听
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 全局接口 > 旋转表冠事件监听
category: harmonyos-references
scraped_at: 2026-09-02T15:01:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f7efa8a19f71a82bf43d121ce1f6f7204296d877ca7695dd6811040d32745f78
---

本模块提供为当前页面设置旋转表冠事件监听器的能力，支持注册页面级的旋转表冠事件监听器，适用于需要感知旋转表冠操作并进行页面级交互处理的场景。仅支持配备旋转表冠的设备。

**说明** 

本模块首批接口从API version 24开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## setMonitorForCrownEvents

setMonitorForCrownEvents(handler: Function): void

为当前页面设置旋转表冠事件监听器，当旋转表冠事件触发时，监听器会触发回调。

该监听器在发生[页面路由](js-apis-router.md)时将自动移除，使用[clearMonitorForCrownEvents()](js-lite-common-monitorcrownevents.md#clearmonitorforcrownevents)接口可手动移除。

**说明** 

* 当发生页面路由时，监听器将自动移除，因此建议在页面的onShow[生命周期](js-lite-framework-lifecycle.md)回调中调用此接口。
* 每个页面仅支持设置一个监听器，新注册的监听器会覆盖之前的监听器，系统将使用最后一次调用此接口时传入的监听器。
* 请勿在[app.js](../harmonyos-guides/js-framework-js-file.md)中使用此函数，其行为未定义。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**模型约束：** 此接口仅可在FA模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Function | 是 | 旋转表冠事件发生后执行该回调。回调格式为(event)=>{ return false/true; }。  返回true时，旋转表冠事件不再分发给获焦的组件。  返回false时，旋转表冠事件会继续分发给获焦组件。当回调的返回值异常时，例如返回值为undefined或无返回值，默认取值为false。  可通过入参获取旋转表冠事件信息，事件信息请参见**表1 CrownEvent对象属性列表**。 |

**表1** CrownEvent对象属性列表

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳，单位ns。 |
| angularVelocity | number | 否 | 否 | 旋转角速度，表示每秒转的角度。  逆时针旋转表冠时旋转角速度为正数，顺时针旋转表冠时旋转角速度为负数。  单位：deg/s |
| degree | number | 否 | 否 | 相对旋转角度。  逆时针旋转表冠时相对旋转角度为正数，顺时针旋转表冠时相对旋转角度为负数。  单位：deg。  取值范围：[-360, 360] |

## clearMonitorForCrownEvents

clearMonitorForCrownEvents(): void

清除当前页面的旋转表冠事件监听器。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**模型约束：** 此接口仅可在FA模型下使用。

## 示例

### 示例1（设置旋转表冠事件监听器）

该示例介绍如何通过[setMonitorForCrownEvents](js-lite-common-monitorcrownevents.md#setmonitorforcrownevents)为页面设置旋转表冠事件监听器，并通过监听器的回调返回值控制Slider组件是否响应旋转表冠事件。

从API version 24开始，新增[setMonitorForCrownEvents](js-lite-common-monitorcrownevents.md#setmonitorforcrownevents)接口和[clearMonitorForCrownEvents](js-lite-common-monitorcrownevents.md#clearmonitorforcrownevents)接口。

```css
/* xxx.css */
.container {
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
}
.title {
    width: 80%;
    font-size: 30px;
    text-align: center;
    border-width: 2px;
    border-color: aliceblue;
    margin: 5px;
}
```

```html
<!-- xxx.hml -->
<div class="container">
    <text class="title" onclick="flagChange">flagChange</text>
    <text class="title" onclick="clearMonitor">clearMonitor</text>
    <text>slider start value is {{startValue}}</text>
    <text>slider current value is {{currentValue}}</text>
    <text>slider end value is {{endValue}}</text>
    <slider min="0" max="100" value="{{value}}" ref="sliderObj"
            onchange="setValue" style="margin-top: 10%; width: 80%;height: 1%"></slider>
</div>
```

```js
// xxx.js
export default {
    data: {
        value: 0,
        startValue: 0,
        currentValue: 0,
        endValue: 100,
        flag: false
    },
    onShow() {
        this.$refs.sliderObj.rotation({ focus: true });
        setMonitorForCrownEvents((event) => {
            console.error('event.timestamp: ' + event.timestamp + '\n' + 'event.angularVelocity: ' +
            event.angularVelocity + '\n' + 'event.degree:' + event.degree);
            return this.flag;
        });
    },
    setValue(e) {
        this.currentValue = e.value;
    },
    clearMonitor() {
        clearMonitorForCrownEvents();
    },
    flagChange() {
        this.flag = !this.flag;
    }
}
```
