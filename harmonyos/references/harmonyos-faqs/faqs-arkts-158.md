---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-158
title: 编译时class-transformer中-Type报错该如何解决
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 编译时class-transformer中-Type报错该如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d23c14683509f15067e45ff9ed05204534a63b2d7db6e0bea6f124b9ddce2165
---

## 问题现象

在ArkTS中使用class-transformer库的@Type注解时，与ArkTS的V2版本状态管理中@Type的注解冲突，导致编译器代码检查不通过。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/mGWZTIseSXWyvGNcMTwL_w/zh-cn_image_0000002629058988.png "点击放大")

## 背景知识

1. 在ArkTS中，想要将从后端接收的JSON数据或者本地JSON数据转为明确的类结构，最常见的方法就是用as Class直接指定，但是这种写法有一个问题，就是as后的Class中类的方法丢失了，例如下面的代码，使用DataBean中的isOk()方法时，会报错提示找不到该方法。

   **代码示例如下：**

   ```ts
   class DataBean {
     code = -1
     msg = ""

     isOk() {
       return this.code == 0
     }
   }

   let json = `{"code":0,"msg":"success"}`
   let dataBean = JSON.parse(json) as DataBean
   hilog.info(0xFF, "[class-transformer]", dataBean.msg) // success
   hilog.info(0xFF, "[class-transformer]", `${dataBean.isOk()}`) // 报错：Error message:undefined is not callable
   ```

   这个主要是因为没有通过构造函数生成对象，用JSON.parse()获得的对象字面量没有对应的[原型链](https://developer.huawei.com/consumer/cn/forum/topic/0201271808808150103?fid=23)，调用不了类方法。
2. 出于上述原因，有开发者开发出了[class-transformer工具库](https://ohpm.openharmony.cn/#/cn/detail/class-transformer-arkts)，并提供方法可以通过传入类的构造函数和对应的JSON数据直接构造出对应的类对象，在代码写法上比从JSON对象字面量取值后再去调用类的构造函数方便许多。class-transformer常见的转换对象用法如下：

   **plainToInstance**：

   此方法将普通ArkTS对象转换为特定类的实例。

   ```ts
   import { plainToInstance } from 'class-transformer';
   let users = plainToInstance(User, userJson); // 将用户纯对象转换为单个用户。还支持数组
   ```

   **instanceToPlain**：

   这个方法将你的类对象转换回普通的ArkTS对象。

   ```ts
   import { instanceToPlain } from 'class-transformer';
   let photo = instanceToPlain(photo);
   ```
3. 当试图转换有嵌套对象的对象时，它需要知道你要转换的对象的类型。因为ArkTS本身没有很好的反射能力，我们应该隐式地指定每个属性包含的对象类型。这是使用class-transformer库中的@Type装饰器完成的。

   **代码示例如下：**

   ```ts
   import { Type, plainToInstance } from 'class-transformer'
   import 'reflect-metadata'
   import { hilog } from '@kit.PerformanceAnalysisKit'

   export class Bean {
     @Type(() => Data)
     data?: Data
   }

   export class Data {
     name?: string
     age?: number

     getName(): string | undefined {
       return this.name
     }
   }

   let json = '{"data":{"name":"张三","age":18}}'
   let bean = plainToInstance(Bean, JSON.parse(json))
   // bean.data就是一个实实在在的Data对象，可以调用getName()方法
   hilog.info(0xFF, "[class-transformer]", `name:${bean.data?.getName()}`) // name:张三
   ```

## 问题定位

从IDE的报错可以看出来，是ArkTS语言框架的注解和class-transformer的注解关键字冲突了。要解决这个问题可以考虑从关键字修改或者引用修改入手。

## 分析结论

由于语言框架提供的@Type注解开发者无法改动，只能从调用三方库的写法入手。通过在导入class-transformer的@Type注解时给其起个别名，就可以规避和V2版本状态管理中@Type注解冲突的问题。

## 解决方案

在代码中导入class-transformer的@Type注解时，给其另起个别名即可解决。

**代码示例如下：**

```ts
import { plainToInstance, Type as ClzTransType } from 'class-transformer';
import { hilog } from '@kit.PerformanceAnalysisKit';
import 'reflect-metadata'; // 需要在ohpm中下载并引入该库，否则class-transformer的@Type会运行错误

class User {
  name: string = '';

  getName(): string {
    return this.name;
  }
}

class RUser {
  sex: number = 0;

  @ClzTransType(() => User)
  user?: User;
}
let json = '{"sex":0,"user":{"name":"张三"}}';
let rUser = plainToInstance(RUser, JSON.parse(json));
hilog.info(0xFF, "[class-transformer]", `name: ${rUser.user?.getName()}`); // name:张三
```

**依赖引入：**

运行示例代码前，需要执行ohpm install class-transformer和ohpm install reflect-metadata安装三方依赖包。

## 总结

当在代码中调用工具库遇到声明（包括变量、方法或者类等）与语言框架冲突时，可以在导入时通过给对应声明主体起别名来规避解决。
