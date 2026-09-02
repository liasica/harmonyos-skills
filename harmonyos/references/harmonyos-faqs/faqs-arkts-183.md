---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-183
title: 如何给泛型实例化
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何给泛型实例化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:551a352dc8d1577b81386d3cf53d3b67c2abdc4c810907abb9e68a400e6e16c3
---

## 问题现象

如何将Record<string, any>类型或JSON字符串等简单数据，转换为指定泛型类型的实例对象，且保证对象的属性值可访问、方法可调用？

## 背景知识

1. **泛型类型无法直接实例化**

   TypeScript中的泛型类型（如T）仅在编译时存在，运行时无实际类型信息，因此不能使用new T()或类似语法创建实例，否则会报错：

   ```txt
   'T' only refers to a type, but is being used as a value here
   ```
2. **JSON.parse(str) as T只能生成“纯数据对象”**

   通过JSON.parse转换后，虽然属性值能正确赋值，但该对象**没有原型链和方法绑定**，因此无法调用类中的方法，导致运行时错误。
3. **class-transformer是实现“方法可调用对象”的关键工具**

   plainToClass方法可将普通对象（plain object）转换为具有完整类结构（包括构造函数、原型链、方法等）的实例对象，是解决泛型实例化后方法不可用的关键方案。

## 解决方案

1. 在项目中打开终端运行以下命令，引入三方库class-transformer

   **ohpm install class-transformer**
2. **基类定义（增强安全性与可维护性）**

   ```ts
   /**
    * 基类对象
    */
   export class BaseClass {
     id: number = 1;
     name: string = 'a';

     constructor(value?: Record<string, Object>) {
       if (value) {
         this.fromJson(value);
       }
     }

     fromJson(value: Record<string, Object>) {
       hilog.info(0x0000, 'testTag', 'BaseClass fromJson');
       this.id = value['id'] as number;
       this.name = value['name'] as string;
     }
   }
   ```
3. **泛型实例化工具类（支持属性与方法调用）**

   ```ts
   /**
    * 当前只实现参数 V 为类似 Record<string, Object> 类对象的方案，如果是其他自定义对象可以根据需要修改
    */
   export class TransformClass<T, O> {
     public transfer(paramObj: O): T {
       let str = JSON.stringify(paramObj);
       let obj: T = JSON.parse(str) as T;
       return obj;
     }
   }

   // 基础（简单）类型数据
   let record: Record<string, Object> = {
     'id': 123,
     'name': 'abc',
     'flag': true
   };

   // 实例化三方工具类
   let transformBaseObj = new TransformClass<BaseClass, Record<string, Object>>();

   // 调用三方工具类转换方法将基础（简单）对象数据转换为指定泛型对象
   let baseObj = transformBaseObj.transfer(record);
   // 调用三方库class-transformer中的plainToClass方法使实例化后的泛型对象方法可调用
   baseObj = plainToClass(BaseClass, baseObj);
   ```
4. **完整使用示例（支持属性、方法调用）**

   ```ts
   import { plainToClass } from 'class-transformer';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   /**
    * 基类对象
    */
   export class BaseClass {
     id: number = 1;
     name: string = 'a';

     constructor(value?: Record<string, Object>) {
       if (value) {
         this.fromJson(value);
       }
     }

     fromJson(value: Record<string, Object>) {
       hilog.info(0x0000, 'testTag', 'BaseClass fromJson');
       this.id = value['id'] as number;
       this.name = value['name'] as string;
     }
   }

   /**
    * 当前只实现参数 V 为类似 Record<string, Object> 类对象的方案，如果是其他自定义对象可以根据需要修改
    */
   export class TransformClass<T, O> {
     public transfer(paramObj: O): T {
       let str = JSON.stringify(paramObj);
       let obj: T = JSON.parse(str) as T;
       return obj;
     }
   }

   // 基础（简单）类型数据
   let record: Record<string, Object> = {
     'id': 123,
     'name': 'abc',
     'flag': true
   };

   // 实例化三方工具类
   let transformBaseObj = new TransformClass<BaseClass, Record<string, Object>>();

   // 调用三方工具类转换方法将基础（简单）对象数据转换为指定泛型对象
   let baseObj = transformBaseObj.transfer(record);
   // 调用三方库class-transformer中的plainToClass方法使实例化后的泛型对象方法可调用
   baseObj = plainToClass(BaseClass, baseObj);

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         Button('属性泛型实例化').onClick(() => {
           hilog.info(0x0000, 'testTag', 'Parent.id = ' + baseObj.id);
           hilog.info(0x0000, 'testTag', 'Parent.name = ' + baseObj.name);
         });
         Button('方法泛型实例化').onClick(() => {
           // plainToClass 转换后方法调用也成功
           baseObj.fromJson(record);
         });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 常见FAQ

Q：为什么JSON.parse(str) as T无法调用对象方法？

A：因为JSON.parse生成的是“裸对象”，没有原型链，也没有绑定类的方法。即使as T做类型断言，运行时仍是普通对象，无法调用fromJson等方法。
