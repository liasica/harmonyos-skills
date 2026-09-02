---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1071
title: 如何解决使用@State修饰对象数组，数据变化时页面不刷新问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决使用@State修饰对象数组，数据变化时页面不刷新问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:04+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:bc396e46af927024c0739703ed86d498d636c6b1df74d5adc2ff176fb5ed2bb5
---

## 问题现象

* 场景一：使用@State修饰对象数组，未使用@Observed/@ObjectLink装饰器进行深度观测，所以修改深层属性时，页面不刷新。问题代码如下：

  ```ts
  class SceneOnePerson {
  name: string;
  age: number;

  constructor(name: string, age: number) {
  this.name = name;
  this.age = age;
  }
  }

  @Entry
  @Component
  struct SceneOne {
  @State persons: SceneOnePerson[] = [
  new SceneOnePerson('小张', 12),
  new SceneOnePerson('小赵', 13),
  new SceneOnePerson('小李', 14),
  new SceneOnePerson('小王', 15),
  ];

  build() {
  Column({ space: 10 }) {
  ForEach(this.persons, (curPerson: SceneOnePerson) => {
  Column() {
  Text(`姓名${curPerson.name}`)
  .fontSize(20)
  .fontWeight(FontWeight.Bold);
  Text(`年龄${curPerson.age}`)
  .fontSize(15)
  .fontWeight(FontWeight.Regular);
  };
  });
  Button('修改对象数组属性-修改小张年龄+1')
  .onClick(() => {
  this.persons[0].age++;
  console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
  });
  Button('修改对象数组属性-修改小赵年龄+1')
  .onClick(() => {
  this.persons[1].age++;
  console.info(`当前小赵的年龄为${JSON.stringify(this.persons[1])}`);
  });
  }
  .height('100%')
  .width('100%')
  .justifyContent(FlexAlign.Center);
  }
  }
  ```

* 场景二：使用了@Observed/@ObjectLink装饰器进行深度观测，由于@ObjectLink只能观察一层属性导致的页面不刷新。

  ```ts
  @Observed
  class PerInfo {
  name: string;
  age: number;
  friends: PerInfo[];

  constructor(model: PerInfoModel) {
  this.name = model.name;
  this.age = model.age;
  this.friends = model.friends.map(friend => new PerInfo(friend));
  }
  }

  interface PerInfoModel {
  name: string;
  age: number;
  friends: PerInfoModel[];
  }

  @Component
  struct SceneTwoFirstChild {
  @ObjectLink info: PerInfo; // 必须创建子组件，并用@ObjectLink接收数据。

  build() {
  Column({ space: 10 }) {
  Text('这是一个页面')
  .fontSize(20);
  Text(this.info.name)
  .fontSize(16)
  .onClick(() => {
  this.info.name += '!';
  });
  Text(this.info.age.toString())
  .fontSize(16)
  .onClick(() => {
  this.info.age++;
  });
  ForEach(this.info.friends, (item: PerInfo) => {
  Column({ space: 10 }) {
  Button(`${item.name}`)
  .onClick(() => {
  item.name += '!';
  console.info(item.name);
  });
  Button(`${item.age}`)
  .onClick(() => {
  item.age++;
  console.info(item.age.toString());
  });
  };
  });
  };
  }
  }

  @Entry
  @Component
  struct SceneTwo {
  @State infos: PerInfo = new PerInfo({
  name: 'Tom',
  age: 18,
  friends: [
  {
  name: 'Jerry',
  age: 18,
  friends: [{ name: 'Tom', age: 20, friends: [] }]
  },
  {
  name: 'Mike',
  age: 18,
  friends: [{ name: 'Nancy', age: 20, friends: [] }]
  }
  ]
  });

  build() {
  Column({ space: 15 }) {
  SceneTwoFirstChild({ info: this.infos });
  }
  .width('100%')
  .height('100%');
  }
  }
  ```
* 场景三：使用了@Observed/@ObjectLink装饰器进行深度观测，由于ForEach首次渲染与非首次渲染引起的页面不刷新。

  ```ts
  @Observed
  class SceneThreePerson {
  name: string;
  age: number;

  constructor(name: string, age: number) {
  this.name = name;
  this.age = age;
  }
  }

  @Component
  struct SceneThreeChild {
  @ObjectLink person: SceneThreePerson;

  build() {
  Column() {
  Text(`姓名${this.person.name}`)
  .fontSize(20)
  .fontWeight(FontWeight.Bold);
  Text(`年龄${this.person.age}`)
  .fontSize(15)
  .fontWeight(FontWeight.Regular);
  };
  }
  }

  @Entry
  @Component
  struct SceneThree {
  @State persons: SceneThreePerson[] = [
  new SceneThreePerson('小张', 12),
  new SceneThreePerson('小赵', 13),
  new SceneThreePerson('小李', 14),
  new SceneThreePerson('小王', 15),
  ];

  build() {
  Column({ space: 10 }) {
  ForEach(this.persons, (curPerson: SceneThreePerson) => {
  SceneThreeChild({ person: curPerson });
  });
  Button('修改对象数组属性-修改小张年龄+1')
  .onClick(() => {
  this.persons[0].age++;
  console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
  });
  Button('替换对象数组元素-修改小张年龄为88')
  .onClick(() => {
  this.persons.splice(0, 1, new SceneThreePerson('小张', 88));
  console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
  });
  }
  .height('100%')
  .width('100%')
  .justifyContent(FlexAlign.Center);
  }
  }
  ```

  场景三问题现象如下，当想要将小张的年龄第二次修改为88时（89修改为88）UI不刷新：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/LxMbcraTQp2dgFlbkDDvyg/zh-cn_image_0000002689362454.png "点击放大")

## 背景知识

* [@State装饰的变量](../harmonyos-guides/arkts-state.md)，或称为状态变量，一旦变量拥有了状态属性，就可以触发其直接绑定UI组件的刷新。当状态改变时，UI会发生对应的渲染改变。@State装饰器仅能观察到第一层的变化，但是在实际应用开发中，应用会根据开发需要，封装自己的数据模型。对于多层嵌套的情况，比如二维数组、对象数组，或者对象内嵌套对象，他们的第二层的属性变化是无法观察到的。例如：当装饰对象为对象数组时，可以观察到数组本身的赋值和添加、删除、更新数组的变化，但是数组项中属性的赋值观察不到。
* [@Observed/@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)、[@ObservedV2/@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)等，可用于嵌套场景的观察，可以用来观察二维数组、数组项Class、Class的属性是Class，这些深层的属性变化。@Observed/@ObjectLink修饰的对象，没有通过new的方式实例化时，不会具备深度观测的能力。比如通过JSON.parse()的方式反序列化的对象，即使被@Observed/@ObjectLink装饰器修饰，也不会具备深度观测的能力。
* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)接口基于数组类型数据来进行循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。当ForEach组件进行非首次渲染时，ForEach会根据传入的键值进行匹配，如果没有匹配到相同的键值则会创建一个新的组件，而当键值已存在则不会创建新的组件，前后的keyGenerator参数一致会导致无法刷新UI，ForEach参数介绍详见：[ForEach参数介绍](../harmonyos-references/ts-rendering-control-foreach.md#接口)。

## 解决方案

@State装饰的变量可以观察到简单类型的变量值变化，在状态管理V1中要想观察到Class中对象类型的某个属性的变化，可以使用@Observed/@ObjectLink装饰器。同时，需要注意是否违背装饰器的限制条件，以及是否违背其它组件原则，常见问题现象总结及解决方案如下：

| 场景 | 场景描述 | 解决方案 |
| --- | --- | --- |
| 场景一 | 使用@State修饰对象数组，未使用@Observed/@ObjectLink装饰器进行深度观测，所以修改深层属性时，页面不刷新。 | 使用@Observed修饰类，使用@ObjectLink在子组件中接收需要深层观测的对象，且该对象若想要被深度观测必须使用new操作符实例化。 |
| 场景二 | 使用了@Observed/@ObjectLink装饰器进行深度观测，由于@ObjectLink只能观察一层属性导致的页面不刷新。 | @ObjectLink仅能观察其代理的属性，无法观察到代理属性的嵌套对象属性，所以每一层被嵌套的对象都需要封装一个子组件并用@ObjectLink接收。 |
| 场景三 | 使用了@Observed/@ObjectLink装饰器进行深度观测，由于ForEach首次渲染与非首次渲染引起的页面不刷新。 | 应尽量避免状态管理的对象深层嵌套的属性刷新与ForEach针对数组变化的首次渲染刷新，若无法避免可采用以下两种方式解决：  1. 重写系统默认的keyGenerator参数生成规则，加入每次修改的当前时间等唯一性的参数，保证前后两次依靠ForEach首次渲染刷新时，keyGenerator不会重复。  2. 不重写系统默认的keyGenerator参数生成规则，给对象数组的每一个对象添加一个唯一的id标识，保证前后两次依靠ForEach首次渲染刷新时，keyGenerator不会重复。 |

* 场景一：使用@State修饰对象数组，未使用@Observed/@ObjectLink装饰器进行深度观测，所以修改深层属性时，页面不刷新。

  使用@Observed修饰类，使用@ObjectLink在子组件中接收需要深层观测的对象，且该对象若想要被深度观测必须使用new操作符实例化。

  示例代码如下：

  ```ts
  @Observed
  class SceneOnePerson {
    name: string;
    age: number;

    constructor(name: string, age: number) {
      this.name = name;
      this.age = age;
    }
  }

  @Component
  struct SceneOneChild {
    @ObjectLink person: SceneOnePerson;

    build() {
      Column() {
        Text(`姓名${this.person.name}`)
          .fontSize(20)
          .fontWeight(FontWeight.Bold);
        Text(`年龄${this.person.age}`)
          .fontSize(15)
          .fontWeight(FontWeight.Regular);
      };
    }
  }

  @Entry
  @Component
  struct SceneOne {
    @State persons: SceneOnePerson[] = [
      new SceneOnePerson('小张', 12),
      new SceneOnePerson('小赵', 13),
      new SceneOnePerson('小李', 14),
      new SceneOnePerson('小王', 15),
    ];

    build() {
      Column({ space: 10 }) {
        ForEach(this.persons, (curPerson: SceneOnePerson) => {
          SceneOneChild({ person: curPerson });
        });
        Button('修改对象数组属性-修改小张年龄+1')
          .onClick(() => {
            this.persons[0].age++;
            console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
          });
        Button('修改对象数组属性-修改小赵年龄+1')
          .onClick(() => {
            this.persons[1].age++;
            console.info(`当前小赵的年龄为${JSON.stringify(this.persons[1])}`);
          });
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center);
    }
  }
  ```

  **说明** 

  如果存在@Observed装饰的类没有使用new操作符实例化的情况、或者存在无法使用@Observed装饰器装饰类的情况时，也无法刷新页面。可以通过[makeV1observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)、[makeObserved](../harmonyos-references/js-apis-statemanagement.md#makeobserved)方法将对象转化为可深度观测的对象，再进行刷新。适用的场景详见官网链接：[概述](../harmonyos-guides/arkts-new-makeobserved.md#概述)。

  场景一实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/IUn9mv3hTQeHMsQoICZwhw/zh-cn_image_0000002689210526.png "点击放大")

* 场景二：使用了@Observed/@ObjectLink装饰器进行深度观测，由于@ObjectLink只能观察一层属性导致的页面不刷新。

  当@ObjectLink修饰的变量含有嵌套类对象时，组件修改嵌套对象的属性，无法刷新UI。因为@ObjectLink仅能观察其代理的属性，无法观察到代理属性的嵌套对象属性。参考：[复杂嵌套对象属性更改失效](../harmonyos-guides/arkts-observed-and-objectlink.md#复杂嵌套对象属性更改失效)。每一层被嵌套的对象都需要封装一个子组件并用@ObjectLink接收，才能实现页面刷新。

  1. 使用@Observed分别修饰双层嵌套的类。
  2. 自定义子组件SceneThreeFirstChild和SceneThreeSecondChild分别接收对应层级的对象，注意@ObjectLink装饰器不能在@Entry装饰的自定义组件中使用。

  示例代码如下：

  ```ts
  @Observed
  class PerInfo {
    name: string;
    age: number;
    friends: PerInfo[];

    constructor(model: PerInfoModel) {
      this.name = model.name;
      this.age = model.age;
      this.friends = model.friends.map(friend => new PerInfo(friend));
    }
  }

  interface PerInfoModel {
    name: string;
    age: number;
    friends: PerInfoModel[];
  }

  @Component
  struct SceneTwoFirstChild {
    @ObjectLink info: PerInfo; // 必须创建子组件，并用@ObjectLink接收数据。

    build() {
      Column({ space: 10 }) {
        Text('这是一个页面')
          .fontSize(20);
        Text(this.info.name)
          .fontSize(16)
          .onClick(() => {
            this.info.name += '!';
          });
        Text(this.info.age.toString())
          .fontSize(16)
          .onClick(() => {
            this.info.age++;
          });
        ForEach(this.info.friends, (item: PerInfo) => {
          SceneTwoSecondChild({ info: item });
        });
      };
    }
  }

  @Component
  struct SceneTwoSecondChild {
    @ObjectLink info: PerInfo; // 必须创建子组件，并用@ObjectLink接收数据。

    build() {
      Column({ space: 10 }) {
        Button(`${this.info.name}`)
          .onClick(() => {
            this.info.name += '!';
            console.info(this.info.name);
          });
        Button(`${this.info.age}`)
          .onClick(() => {
            this.info.age++;
            console.info(this.info.age.toString());
          });
      };
    }
  }

  @Entry
  @Component
  struct SceneTwo {
    @State infos: PerInfo = new PerInfo({
      name: 'Tom',
      age: 18,
      friends: [
        {
          name: 'Jerry',
          age: 18,
          friends: [{ name: 'Tom', age: 20, friends: [] }]
        },
        {
          name: 'Mike',
          age: 18,
          friends: [{ name: 'Nancy', age: 20, friends: [] }]
        }
      ]
    });

    build() {
      Column({ space: 15 }) {
        SceneTwoFirstChild({ info: this.infos });
      }
      .width('100%')
      .height('100%');
    }
  }
  ```

  场景二实现效果如下，嵌套对象的每个层级的属性都可以实现UI刷新：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/iH6rmNpLS0SwPQls9cr65g/zh-cn_image_0000002689535616.png "点击放大")

* 场景三：使用了@Observed/@ObjectLink装饰器进行深度观测，由于ForEach首次渲染与非首次渲染引起的页面不刷新。

  当数组对象只修改对象的属性时，不会出现ForEach组件创建规则导致UI不刷新的问题。当数组存在替换或修改数组项时，页面的刷新需要考虑到[ForEach循环渲染](../harmonyos-guides/arkts-rendering-control-foreach.md)中的键值生成规则与组件创建规则，导致的刷新问题。如果ForEach组件的keyGenerator创建规则函数缺省，框架默认的keyGenerator生成函数为(item: T, index: number) => { return index + '\_\_' + JSON.stringify(item); }。

  参考系统默认的keyGenerator创建规则，针对场景三问题代码现象中每一步修改的keyGenerator分析表如下：

  1. 初次创建时ListItem对应的，keyGenerator如下：

     | ListItem显示内容 | keyGenerator |
     | --- | --- |
     | 姓名小张 年龄12 | 0\_\_{"name":"小张","age":12} |
     | 姓名小赵 年龄13 | 1\_\_{"name":"小赵","age":13} |
     | 姓名小李 年龄14 | 2\_\_{"name":"小李","age":14} |
     | 姓名小王 年龄15 | 3\_\_{"name":"小王","age":15} |
  2. 修改小张年龄属性为13，keyGenerator如下：

     | ListItem显示内容 | keyGenerator |
     | --- | --- |
     | 姓名小张 年龄13 | 0\_\_{"name":"小张","age":12} |
     | 姓名小赵 年龄13 | 1\_\_{"name":"小赵","age":13} |
     | 姓名小李 年龄14 | 2\_\_{"name":"小李","age":14} |
     | 姓名小王 年龄15 | 3\_\_{"name":"小王","age":15} |

     **说明** 

     对象数组中对象属性的修改不会刷新keyGenerator，只有修改数组会触发ForEach重新刷新，从而刷新keyGenerator。此时刷新不依靠组件重建，而是依靠状态管理刷新。
  3. 通过修改数组项，修改小张年龄属性为88，keyGenerator如下：

     | ListItem显示内容 | keyGenerator |
     | --- | --- |
     | 姓名小张 年龄88 | 0\_\_{"name":"小张","age":88} |
     | 姓名小赵 年龄13 | 1\_\_{"name":"小赵","age":13} |
     | 姓名小李 年龄14 | 2\_\_{"name":"小李","age":14} |
     | 姓名小王 年龄15 | 3\_\_{"name":"小王","age":15} |

     **说明** 

     修改的数组项，会触发keyGenerator刷新，使得ForEach重建小张所在的组件，并将小张的年龄刷新为88。
  4. 修改小张年龄属性为89，keyGenerator如下：（实现原理与第2步一致，都是状态管理深层嵌套对象属性的刷新，没有直接修改数组属于ForEach的非首次渲染。）

     | ListItem显示内容 | keyGenerator |
     | --- | --- |
     | 姓名小张 年龄89 | 0\_\_{"name":"小张","age":88} |
     | 姓名小赵 年龄13 | 1\_\_{"name":"小赵","age":13} |
     | 姓名小李 年龄14 | 2\_\_{"name":"小李","age":14} |
     | 姓名小王 年龄15 | 3\_\_{"name":"小王","age":15} |
  5. 重置小张年龄属性为88，keyGenerator如下：

     | ListItem显示内容 | keyGenerator |
     | --- | --- |
     | 姓名小张 年龄89 | 0\_\_{"name":"小张","age":88} |
     | 姓名小赵 年龄13 | 1\_\_{"name":"小赵","age":13} |
     | 姓名小李 年龄14 | 2\_\_{"name":"小李","age":14} |
     | 姓名小王 年龄15 | 3\_\_{"name":"小王","age":15} |

     **说明** 

     发现第5步中无论是ListItem显示内容与keyGenerator都未发生变化。原因是通过替换数组项或数组触发的ForEach刷新，刷新的规则是刷新前后的keyGenerator不一致才会刷新，但是通过对比上述表格中的keyGenerator发现：第3步、第4步、第5步小张所在的组件对应的keyGenerator都没有变化，所以不会触发ForEach重建刷新。

     **综上所述**：当数据是对象数组时，若同时存在状态管理的对象深层嵌套的属性刷新与ForEach针对数组变化的首次渲染刷新时，应尽量避免使用两种方式交替刷新UI。若无法避免可参考以下解决方案：

     + 方案一：重写系统默认的keyGenerator参数生成规则，加入每次修改的当前时间等唯一性的参数，保证前后两次依靠ForEach首次渲染刷新时，keyGenerator不会重复。示例代码如下：

       ```ts
       @Observed
       class SceneThreeOptionOnePerson {
         name: string;
         age: number;

         constructor(name: string, age: number) {
           this.name = name;
           this.age = age;
         }
       }

       @Component
       struct SceneThreeOptionOneChild {
         @ObjectLink person: SceneThreeOptionOnePerson;

         build() {
           Column() {
             Text(`姓名${this.person.name}`)
               .fontSize(20)
               .fontWeight(FontWeight.Bold);
             Text(`年龄${this.person.age}`)
               .fontSize(15)
               .fontWeight(FontWeight.Regular);
           };
         }
       }

       @Entry
       @Component
       struct SceneThreeOptionOne {
         @State persons: SceneThreeOptionOnePerson[] = [
           new SceneThreeOptionOnePerson('小张', 12),
           new SceneThreeOptionOnePerson('小赵', 13),
           new SceneThreeOptionOnePerson('小李', 14),
           new SceneThreeOptionOnePerson('小王', 15),
         ];

         build() {
           Column({ space: 10 }) {
             ForEach(this.persons, (curPerson: SceneThreeOptionOnePerson) => {
               SceneThreeOptionOneChild({ person: curPerson });
             }, (item: SceneThreeOptionOnePerson, index: number) => {
               console.info(`${index}'__'${JSON.stringify(item)}${JSON.stringify(Date.now())}`); // 打印keyGenerator
               return index + '__' + JSON.stringify(item) + JSON.stringify(Date.now()); // 加入Date.now()避免重复
             });
             Button('修改对象数组属性-修改小张年龄为+1')
               .onClick(() => {
                 this.persons[0].age++;
                 console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
               });
             Button('替换对象数组元素-修改小张年龄为88')
               .onClick(() => {
                 this.persons.splice(0, 1, new SceneThreeOptionOnePerson('小张', 88));
                 console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
               });
           }
           .height('100%')
           .width('100%')
           .justifyContent(FlexAlign.Center);
         }
       }
       ```
     + 方案二：不重写系统默认的keyGenerator参数生成规则，给对象数组的每一个对象添加一个唯一的id标识，保证前后两次依靠ForEach首次渲染刷新时，keyGenerator不会重复。示例代码如下：

       ```ts
       @Observed
       class SceneThreeOptionTwoPerson {
         name: string;
         age: number;
         id: string; // 给每个对象设置一个id

         constructor(name: string, age: number, id: string) {
           this.name = name;
           this.age = age;
           this.id = id;
         }
       }

       @Component
       struct SceneThreeOptionTwoChild {
         @ObjectLink person: SceneThreeOptionTwoPerson;

         build() {
           Column() {
             Text(`姓名${this.person.name}`)
               .fontSize(20)
               .fontWeight(FontWeight.Bold);
             Text(`年龄${this.person.age}`)
               .fontSize(15)
               .fontWeight(FontWeight.Regular);
           };
         }
       }

       @Entry
       @Component
       struct SceneThreeOptionTwo {
         @State persons: SceneThreeOptionTwoPerson[] = [
           new SceneThreeOptionTwoPerson('小张', 12, Date.now().toString()),
           new SceneThreeOptionTwoPerson('小赵', 13, Date.now().toString()),
           new SceneThreeOptionTwoPerson('小李', 14, Date.now().toString()),
           new SceneThreeOptionTwoPerson('小王', 15, Date.now().toString()),
         ];

         build() {
           Column({ space: 10 }) {
             ForEach(this.persons, (curPerson: SceneThreeOptionTwoPerson) => {
               SceneThreeOptionTwoChild({ person: curPerson });
             }); // 使用默认的keyGenerator创建规则
             Button('修改对象数组属性-修改小张年龄为+1')
               .onClick(() => {
                 this.persons[0].age++;
                 console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
               });
             Button('替换对象数组元素-修改小张年龄为88')
               .onClick(() => {
                 // 此处以当前时间作为对象的id
                 this.persons.splice(0, 1, new SceneThreeOptionTwoPerson('小张', 88, Date.now().toString()));
                 console.info(`当前小张的年龄为${JSON.stringify(this.persons[0])}`);
               });
           }
           .height('100%')
           .width('100%')
           .justifyContent(FlexAlign.Center);
         }
       }
       ```

       场景三修复效果如下，重复上述第5步时，发现可以重建刷新UI将小张的年龄从89重置为88：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/QyvsUjz7QPWt553HPlSGgw/zh-cn_image_0000002689399358.png "点击放大")

## 常见FAQ

Q：@ObjectLink装饰器是否能在@Entry装饰的自定义组件中使用？

A：@ObjectLink装饰器是不能在@Entry装饰的自定义组件中使用，且需要搭配@Observed装饰器一起使用。

Q：定义变量来保存图片src参数，在onClick方法中修改src参数，不生效未触发UI渲染，该怎么处理？

A：可以确认下保存参数的变量是否使用@State进行装饰，未使用@State装饰器，修改src值是不会生效的。

Q：@State和@Local使用有什么区别？

A：可以参考[@Local与@State对比](../harmonyos-guides/arkts-new-local.md#local与state对比)，@Local装饰器使用参考[@Local装饰器](../harmonyos-guides/arkts-new-local.md)，@State装饰器的使用参考[@State装饰器](../harmonyos-guides/arkts-state.md)。

Q：对象在UI中刷新渲染是否需要添加@Observed/@ObservedV2装饰器？

A：如果不涉及深度观测，只涉及对象本身的改变，可以不添加@Observed/@ObservedV2装饰器。

Q：嵌套对象中未被@Track装饰器装饰的属性无法刷新UI？

A：是的，如果Class类中使用了@Track装饰器，则未被@Track装饰器装饰的属性不能在UI中使用，如果使用，会发生运行时报错。

Q：@State可以标识基本数据类型的数组，是否可以监听数组的增删？

A：@State可以监听数组的增删，实现UI刷新。

## 总结

1. @State装饰器仅能观察到**第一层**的变化。对于多层嵌套的情况，比如对象数组等，他们的第二层的属性变化是无法观察到的。@Observed装饰的类，可以观察到**属性**的变化；@ObjectLink装饰器装饰的状态变量用于接收@Observed装饰的类的实例，和父组件中对应的状态变量建立**双向数据绑定**。使用时应遵循对应装饰器在官方指南的使用限制。
2. 当数据是对象数组时，若存在状态管理的对象深层嵌套的属性刷新与ForEach针对数组变化的首次渲染刷新时，应尽量避免使用两种方式交替刷新UI。若无法避免可重写系统默认的keyGenerator参数，加入每次修改的当前时间等唯一性的参数，保证前后两次依靠ForEach首次渲染刷新时，keyGenerator不会重复。
