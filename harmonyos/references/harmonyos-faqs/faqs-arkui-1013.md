---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1013
title: "@Monitor如何监听深层属性的变化"
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > @Monitor如何监听深层属性的变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a0b87767d85be66fdf64ca4cf67e07b095378cd580e4d0a96aec9d76c043124f
---

## 问题现象

在使用@Monitor时，应该如何监听深层嵌套的属性变化？同时应该注意哪些事项？

## 背景知识

* [@ObservedV2/@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)：@ObservedV2装饰器与@Trace装饰器用于装饰类以及类中的属性，使得被装饰的类和属性具有深度观测的能力。
* [@Monitor](../harmonyos-guides/arkts-new-monitor.md)：用于监听组件内部状态变量的变化，当被监听的状态变量发生改变时会自动触发回调逻辑。需注意当@Monitor监听的是对象中的属性时，属性需要被@Trace装饰，未被@Trace装饰的属性的变化无法被监听。

## 解决方案

@Monitor支持在@ObservedV2装饰的Class以及UI组件内监听属性的变化，常见深层属性监听的场景总结如下：

| 场景 | 场景描述 | 实现方案 |
| --- | --- | --- |
| 场景一 | @Monitor如何监听嵌套Class内对象属性的变化 | 1. 在@ObservedV2装饰的Class中监听时，通过传入“属性名”到@Monitor内，实现属性监听。  2. 在UI组件中监听时，通过传入“变量名.属性名”到@Monitor内，实现深层属性监听。 |
| 场景二 | @Monitor如何监听对象数组内对象属性的变化 | 1. 在@ObservedV2装饰的Class中监听时，通过传入“属性名”到@Monitor内，实现对象数组内对象的属性监听。  2. 在UI组件中监听时，通过传入“数组名.索引位置.属性名”到@Monitor内，实现对象数组内对象的属性监听。 |
| 场景三 | @Monitor如何监听Map/Set内对象属性的变化 | 在@ObservedV2装饰的Class中监听时，通过传入“属性名”到@Monitor内，实现Map/Set内对象的属性监听。 |

* **场景一**：@Monitor监听嵌套Class对象属性的变化。

  该场景下，@Monitor既能在@ObservedV2装饰的类中监听被@Trace装饰的属性，也能在UI组件中监听被@Trace装饰的属性，完整示例代码如下：

  ```ts
  @ObservedV2
  class InfoOne {
    @Trace phoneNumber: number = 0;

    constructor(phoneNumber: number) {
      this.phoneNumber = phoneNumber;
    }

    // @Monitor可以写在Class中监听属性变化。
    @Monitor('phoneNumber')
    phoneNumberChange(monitor: IMonitor) {
      let lastValue: number = monitor.value()?.before as number;
      let curValue: number = monitor.value()?.now as number;
      console.info(`在Info类中监听phoneNumber属性的变化，变之前的值：${lastValue}，变后的值：${curValue}。`);
    }
  }

  @ObservedV2
  class PersonOne {
    @Trace name: string = '小明';
    @Trace info: InfoOne = new InfoOne(123456789);

    // 监听嵌套类中属性
    @Monitor('info.phoneNumber')
    phoneNumberChange(monitor: IMonitor) {
      let lastValue: number = monitor.value()?.before as number;
      let curValue: number = monitor.value()?.now as number;
      console.info(`在Person类中监听嵌套Info类中的phoneNumber属性的变化，变之前的值：${lastValue}，变后的值：${curValue}。`);
    }

    // 监听自身多个属性变化。
    @Monitor('name', 'info')
    personPropertyChange(monitor: IMonitor) {
      monitor.dirty.forEach((path: string) => {
        console.info(`在Person类中监听${path}属性的变化，变之前的值：${JSON.stringify(monitor.value(path)?.before)}，变后的值：${JSON.stringify(monitor.value(path)?.now)}。`);
      });
    }
  }

  @Entry
  @ComponentV2
  struct SceneOne {
    @Local person: PersonOne = new PersonOne();

    // 多个属性变化。
    @Monitor('person.name', 'person.info', 'person.info.phoneNumber', 'person')
    propertyChange(monitor: IMonitor) {
      monitor.dirty.forEach((path: string) => {
        console.info(`在ComponentV2组件中监听${path}的变化，变之前的值：${JSON.stringify(monitor.value(path)?.before)}，变后的值：${JSON.stringify(monitor.value(path)?.now)}。`);
      });
    }

    build() {
      Column({ space: 15 }) {
        Button('修改Info实例化的属性')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.person.info.phoneNumber = 999999999;
          });
        Button('修改Person实例化的属性')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.person.info = new InfoOne(666666666);
            this.person.name = '小王';
          });
        Button('修改Person')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.person = new PersonOne();
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  依次点击修改，@Monitor监听日志打印如下：

  ```txt
  01-22 14:39:05.416   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person.info.phoneNumber的变化，变之前的值：123456789，变后的值：999999999。
  01-22 14:39:05.416   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在Info类中监听phoneNumber属性的变化，变之前的值：123456789，变后的值：999999999。
  01-22 14:39:05.416   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在Person类中监听嵌套Info类中的phoneNumber属性的变化，变之前的值：123456789，变后的值：999999999。
  01-22 14:39:06.549   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在Person类中监听name属性的变化，变之前的值："小明"，变后的值："小王"。
  01-22 14:39:06.549   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在Person类中监听info属性的变化，变之前的值：{"__ob_phoneNumber":999999999}，变后的值：{"__ob_phoneNumber":666666666}。
  01-22 14:39:06.549   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person.name的变化，变之前的值："小明"，变后的值："小王"。
  01-22 14:39:06.549   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person.info的变化，变之前的值：{"__ob_phoneNumber":999999999}，变后的值：{"__ob_phoneNumber":666666666}。
  01-22 14:39:06.549   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person.info.phoneNumber的变化，变之前的值：999999999，变后的值：666666666。
  01-22 14:39:06.549   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在Person类中监听嵌套Info类中的phoneNumber属性的变化，变之前的值：999999999，变后的值：666666666。
  01-22 14:39:07.104   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person.name的变化，变之前的值："小王"，变后的值："小明"。
  01-22 14:39:07.104   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person.info的变化，变之前的值：{"__ob_phoneNumber":666666666}，变后的值：{"__ob_phoneNumber":123456789}。
  01-22 14:39:07.104   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person.info.phoneNumber的变化，变之前的值：666666666，变后的值：123456789。
  01-22 14:39:07.104   9419-9419     A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听person的变化，变之前的值：{"__ob_name":"小王","__ob_info":{"__ob_phoneNumber":666666666}}，变后的值：{"__ob_name":"小明","__ob_info":{"__ob_phoneNumber":123456789}}。
  ```
* **场景二**：@Monitor监听对象数组内对象属性的变化。
  1. 当@Monitor监听数组整体时，只能观测到数组整体的赋值。且可以通过监听数组的长度变化来判断数组是否有插入、删除等变化。
  2. 若需要监听对象数组中某一个对象的变化，当前仅支持使用"."的方式表达深层属性、数组项的监听，详情参考官网：[通用监听能力](../harmonyos-guides/arkts-new-monitor.md#通用监听能力)。所以在UI组件中使用@Monitor监听对象数组的对象时，使用personArr.0表示数组的第一项，即@Monitor内使用personArr.0代替personArr[0]，完整示例代码如下：

  ```ts
  @ObservedV2
  class InfoTwo {
    @Trace phoneNumber: number = 0;

    constructor(phoneNumber: number) {
      this.phoneNumber = phoneNumber;
    }
  }

  @ObservedV2
  class PersonTwo {
    @Trace name: string = '小明';
    @Trace info: InfoTwo = new InfoTwo(123456789);
  }

  @Entry
  @ComponentV2
  struct SceneTwo {
    @Local personArr: PersonTwo[] = [new PersonTwo()];

    // 多个属性变化，对于数组而言，对数组某一项的监听不是通过“[]”表述索引位置，而是通过“.”获取索引位置。
    @Monitor('personArr.0.name', 'personArr.0.info', 'personArr.0.info.phoneNumber', 'personArr.0')
    propertyChange(monitor: IMonitor) {
      monitor.dirty.forEach((path: string) => {
        console.info(`在ComponentV2组件中监听${path}的变化，变之前的值：${JSON.stringify(monitor.value(path)?.before)}，变后的值：${JSON.stringify(monitor.value(path)?.now)}。`);
      });
    }

    // 监听数组长度变化。
    @Monitor('personArr.length')
    arrChange(monitor: IMonitor) {
      monitor.dirty.forEach((path: string) => {
        console.info(`在ComponentV2组件中监听${path}的变化，变之前的值：${JSON.stringify(monitor.value(path)?.before)}，变后的值：${JSON.stringify(monitor.value(path)?.now)}。`);
      });
    }

    build() {
      Column({ space: 15 }) {
        Button('修改InfoTwo实例化的属性')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 以第一项为例
            this.personArr[0].info.phoneNumber = 999999999;
          });
        Button('修改PersonTwo实例化的属性')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 以第一项为例
            this.personArr[0].info = new InfoTwo(666666666);
            this.personArr[0].name = '小王';
          });
        Button('修改PersonTwo')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 以第一项为例
            this.personArr[0] = new PersonTwo();
          });
        Button('修改增加项数组')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.personArr.push(new PersonTwo());
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  依次点击修改，@Monitor监听日志打印如下：

  ```txt
  01-22 14:40:46.789   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0.info.phoneNumber的变化，变之前的值：123456789，变后的值：999999999。
  01-22 14:40:51.398   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0.name的变化，变之前的值："小明"，变后的值："小王"。
  01-22 14:40:51.398   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0.info的变化，变之前的值：{"__ob_phoneNumber":999999999}，变后的值：{"__ob_phoneNumber":666666666}。
  01-22 14:40:51.398   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0.info.phoneNumber的变化，变之前的值：999999999，变后的值：666666666。
  01-22 14:40:54.587   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0.name的变化，变之前的值："小王"，变后的值："小明"。
  01-22 14:40:54.587   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0.info的变化，变之前的值：{"__ob_phoneNumber":666666666}，变后的值：{"__ob_phoneNumber":123456789}。
  01-22 14:40:54.587   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0.info.phoneNumber的变化，变之前的值：666666666，变后的值：123456789。
  01-22 14:40:54.587   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.0的变化，变之前的值：{"__ob_name":"小王","__ob_info":{"__ob_phoneNumber":666666666}}，变后的值：{"__ob_name":"小明","__ob_info":{"__ob_phoneNumber":123456789}}。
  01-22 14:40:56.293   11869-11869   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听personArr.length的变化，变之前的值：1，变后的值：2。
  ```
* **场景三**：@Monitor监听Map/Set内对象属性的变化。

  由于场景二中提到@Monitor当前仅支持使用"."的方式表达深层属性、数组项的监听。所以当Map/Set内存储的是对象时，建议在@ObservedV2装饰的Class内实现属性监听，而非在UI组件内实现属性监听。同时可以在UI组件内通过监听接口的方式，监听Map/Set增、删等变化。完整代码示例如下：

  ```ts
  @ObservedV2
  class InfoThree {
    @Trace phoneNumber: number = 0;

    constructor(phoneNumber: number) {
      this.phoneNumber = phoneNumber;
    }

    // 若需要监听Map/Set内对象的属性变化，建议在Class中实现
    @Monitor('phoneNumber')
    phoneNumberChange(monitor: IMonitor) {
      let lastValue: number = monitor.value()?.before as number;
      let curValue: number = monitor.value()?.now as number;
      console.info(`在Info类中监听phoneNumber属性的变化，变之前的值：${lastValue}，变后的值：${curValue}。`);
    }
  }

  @Entry
  @ComponentV2
  struct SceneThree {
    @Local memberMap: Map<string, InfoThree> = new Map([['小明', new InfoThree(123456789)]]);
    @Local memberSet: Set<InfoThree> = new Set([new InfoThree(123456789)]);

    // 监听Map大小变化。
    @Monitor('memberMap.size')
    mapChange(monitor: IMonitor) {
      monitor.dirty.forEach((path: string) => {
        console.info(`在ComponentV2组件中监听${path}的变化，变之前的值：${JSON.stringify(monitor.value(path)?.before)}，变后的值：${JSON.stringify(monitor.value(path)?.now)}。`);
      });
    }

    // 监听Set大小变化。
    @Monitor('memberSet.size')
    setChange(monitor: IMonitor) {
      monitor.dirty.forEach((path: string) => {
        console.info(`在ComponentV2组件中监听${path}的变化，变之前的值：${JSON.stringify(monitor.value(path)?.before)}，变后的值：${JSON.stringify(monitor.value(path)?.now)}。`);
      });
    }

    build() {
      Column({ space: 15 }) {
        Button('Map修改小明电话号码')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // Map
            let tempMap: InfoThree = this.memberMap.get('小明') as InfoThree;
            tempMap.phoneNumber = 999999999;
            // Set
            let tempSet: InfoThree = this.memberSet.values().next().value;
            tempSet.phoneNumber = 888888888;
          });
        Button('增加Map/Set数量')
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.memberMap.set('小张', new InfoThree(123456789));
            this.memberSet.add(new InfoThree(123456789));
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  依次点击修改，@Monitor监听日志打印如下：

  ```txt
  01-22 14:41:53.577   13570-13570   A03d00/JSAPP                    com.examp...07977077  I     在Info类中监听phoneNumber属性的变化，变之前的值：123456789，变后的值：999999999。
  01-22 14:41:53.577   13570-13570   A03d00/JSAPP                    com.examp...07977077  I     在Info类中监听phoneNumber属性的变化，变之前的值：123456789，变后的值：888888888。
  01-22 14:41:54.872   13570-13570   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听memberMap.size的变化，变之前的值：1，变后的值：2。
  01-22 14:41:54.872   13570-13570   A03d00/JSAPP                    com.examp...07977077  I     在ComponentV2组件中监听memberSet.size的变化，变之前的值：1，变后的值：2。
  ```

## 总结

使用@Monitor实现深度监听时，应注意以下两点：

1. @Monitor既可以在@ObservedV2装饰的类里面实现属性监听，也可以ComponentV2组件内实现属性监听。当@Monitor监听的是对象中的属性时，属性需要被@Trace装饰，未被@Trace装饰的属性变化无法被监听。
2. @Monitor当前仅支持使用"."的方式表达深层属性、数组项的监听。监听数组某一项变化时，使用personArr.0表示数组的第一项，即@Monitor内使用personArr.0代替personArr[0]。
