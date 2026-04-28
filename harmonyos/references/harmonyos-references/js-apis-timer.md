---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-timer
title: Timer (定时器)
breadcrumb: API参考 > 公共基础能力 > ArkTS API > Timer (定时器)
category: harmonyos-references
scraped_at: 2026-04-28T08:19:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ec7436f60af1a37d12b0505dcb55282f7f4f6d44c05580d763852456147561c3
---

本模块提供基础的定时器能力，支持按照指定的时间执行对应函数。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

在UI界面中使用定时器时，定时器的触发机制会受UI底层原理管控。如果UI界面退到后台，定时器会被冻结。

## setTimeout

PhonePC/2in1TabletTVWearable

setTimeout(handler: Function | string, delay?: number, ...arguments: any[]): number

设置一个定时器，该定时器在定时器到期后执行一个函数。

该定时器在回调被执行后自动删除，或使用clearTimeout()接口手动删除。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Function | string | 是 | 类型为Function表示定时器到期后执行函数；  类型为string则通过Error方式打印string中内容，不进行其他处理。 |
| delay | number | 否 | 延迟的毫秒数，函数的调用会在该延迟之后发生。建议传入整数，若传入小数，会被向下取整。  如果省略该参数，delay取默认值0。  **注意**：  1. 该计时器非精准计时器，实际延迟可能会与预期延迟存在误差。  2. 如果值小于1，会被默认取0。  3. delay值受系统限制，超出2^31 - 1时会溢出，delay值为0。 |
| ...arguments | any[] | 否 | 附加参数，仅当handler类型为Function时生效，作为参数传递给handler。  arguments参数数量少于handler函数参数数量时，未被arguments覆盖的参数会被设为undefined。  arguments参数数量多于handler函数参数数量时，多余的arguments参数会被忽略，但可通过handler函数内部的arguments对象访问。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 该定时器的ID，定时器ID为进程共享，是从0开始顺序增加的整数，无重复值。 |

**示例1**：不带参数。

```
1. setTimeout(() => {
2. console.info('delay 1s');
3. }, 1000);
```

**示例2**：带参数传递给函数(handler为function时参数与arguments参数个数一致)。

```
1. function myFunction(param1: string, param2: string) {
2. console.info(param1, param2);
3. }
4. setTimeout(myFunction, 1000, 'Hello', 'World');
```

**示例3**：带参数传递给函数(handler为function时参数比arguments参数个数少)。

```
1. function myFunction(a: string, b: string) {
2. console.info(a);
3. // Output: hello
4. console.info(b);
5. // Output: world
6. console.info(JSON.stringify(arguments));
7. // Output: {"0":"hello","1":"world","2":"c++","3":"js"}
8. }
9. setTimeout(myFunction, 1000, 'hello', 'world', 'C++', 'js');
```

**示例4**：带参数传递给函数(handler为function时参数比arguments参数个数多)。

```
1. function myFunction(a: string, b: string) {
2. console.info(a);
3. // Output: hello
4. console.info(b);
5. // Output: undefined
6. console.info(JSON.stringify(arguments));
7. // Output: {"0":"hello"}
8. }
9. setTimeout(myFunction, 1000, 'hello');
```

## clearTimeout

PhonePC/2in1TabletTVWearable

clearTimeout(timeoutID?: number): void

可取消通过调用setTimeout()建立的定时器。

定时器对象保存在创建它的线程内，删除定时器时需要在该线程中进行。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeoutID | number | 否 | 要取消定时器的ID，需要与调用setTimeout()设置定时器的返回值一致。如果省略该参数或指定的定时器ID不存在时，不会取消任何定时任务。 |

**示例：**

```
1. let timeoutID = setTimeout(() => {
2. console.info('do after 1s delay.');
3. }, 1000);
4. clearTimeout(timeoutID);
```

## setInterval

PhonePC/2in1TabletTVWearable

setInterval(handler: Function | string, delay: number, ...arguments: any[]): number

重复调用一个函数，在每次调用之间具有固定的时间延迟。

删除该定时器需手动调用clearInterval接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Function | string | 是 | 类型为Function表示定时器到期后执行函数；  类型为string则通过Error方式打印string中内容，不进行其他处理。 |
| delay | number | 是 | 延迟的毫秒数，函数的调用会在该延迟之后发生。建议传入整数，若传入小数，会被向下取整。  如果省略该参数，delay取默认值0。  **注意**：  1. 该计时器非精准计时器，实际延迟可能会与预期延迟存在误差。  2. 如果值小于1，将被默认设置为0。  3. delay值受系统限制，超出2^31 - 1时会溢出，delay值为0。 |
| ...arguments | any[] | 否 | 附加参数，仅当handler类型为Function时生效，作为参数传递给handler。  arguments参数数量少于handler函数参数数量时，未被arguments覆盖的参数会被设为undefined。  arguments参数数量多于handler函数参数数量时，多余的arguments参数会被忽略，但可通过handler函数内部的arguments对象访问。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 该定时器的ID，定时器ID为进程共享，是从0开始顺序增加的整数，无重复值。 |

**示例：**

```
1. setInterval(() => {
2. console.info('do every 1s.');
3. }, 1000);
```

## clearInterval

PhonePC/2in1TabletTVWearable

clearInterval(intervalID?: number): void

可取消通过setInterval()设置的重复定时任务。

定时器对象保存在创建它的线程内，删除定时器时需要在该线程中进行。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| intervalID | number | 否 | 要取消的重复定时器的ID，需要与调用setInterval设置重复定时器的返回值一致。如果省略该参数或指定的重复定时器ID不存在时，不会取消任何定时任务。 |

**示例：**

```
1. let intervalID = setInterval(() => {
2. console.info('do every 1s.');
3. }, 1000);
4. clearInterval(intervalID);
```

## 其他说明

PhonePC/2in1TabletTVWearable

### 超时延迟

如果页面正忙于其他任务，超时可能比预期晚。setTimeout的函数或代码片段在下一个时间周期执行。例如：

```
1. function foo() {
2. console.info('OH test foo is called')
3. }
4. setTimeout(foo, 0);
5. console.info('After OH test setTimeout')

7. // output
8. After OH test setTimeout
9. OH test foo is called
```

这是因为，虽然setTimeout()设置了0ms的延迟，但任务不会立即执行，而是被放入队列中，等待下一次事件循环。当前代码执行完毕后，队列中的函数才会被执行，因此最终的执行顺序可能与预期不一致。

### 最大延迟值

定时器内部使用32位带符号整数存储延时。因此，当延时超过2147483647毫秒（约24.8天）时，定时器会溢出并立即执行。

### 定时器冻结

定时器的触发受底层任务调度。当前应用被切换到后台后，定时器到期不会触发。应用被重新拉起到前台后，到期定时器会按序触发。可以使用trace查看进程是否还存在调度，如果没有调度，定时器会被冻结。

### 定时器ID

setTimeout()和setInterval()使用相同的ID池，因此技术上可以互相调用clearTimeout()和clearInterval()来清除。然而，为了提高代码的可读性和可维护性，建议分别使用各自对应的清除方法，以避免混淆。
