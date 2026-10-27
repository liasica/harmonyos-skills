---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0012
title: ArkTS-JSON数据解析与对象转换常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见问题 > ArkTS-JSON数据解析与对象转换常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:f9630f2bdb7b94a7dfc625e26e2dcf8e39256a1c0cb8eb7af202b5a5fbeb4c54
---

**Q：如何将JSON数据转换成ArkTS中类的实例对象，以便使用实例对象的属性和调用实例对象的方法，并支持嵌套对象的场景？**

**A**：对于这种情况，需要使用第三方库class-transformer和reflect-metadata。通过@Type指定嵌套情况下的类型，然后使用plainToClass转换创建相应的实例对象。

1. 在oh-package.json5中加入第三方库依赖：

   ```json
   {
     "name": "entry",
     "version": "1.0.0",
     "dependencies": {
       "class-transformer": "^0.5.1", // 加入这两行
       "reflect-metadata": "^0.2.2"
     }
   }
   ```
2. 在TS代码中使用如下代码：

   ```ts
   import { Type, plainToClass } from 'class-transformer'
   import "reflect-metadata"

   // Assuming accepted JSON data
   let testJSON: Record<string, ESObject> = {
     'id': 1,
     'firstName': "Johny",
     'lastName': "Cage",
     'age': 27,
     'arr': [
       {
         'name': 'john'
       },
       {
         'name': 'tom'
       }
     ],
     'instanceA': {
       'name': 'john'
     },
   }

   // If there is a corresponding nested structure, the corresponding type needs to be specified
   class A {
     name: string = 'john';

     getName(): string {
       return this.name
     }
   }

   // When attempting to convert an object with nested objects, it is necessary to know the object type to be converted and use the @ Type decorator to implicitly specify the object type contained in each attribute
   class User {
     id: number = 0;
     firstName: string = '';
     lastName: string = '';
     age: number = 0;
     @Type(() => A)
     arr: A[] = [new A()]
     @Type(() => A)
     instanceA: A = new A();

     getName() {
       return this.firstName + " " + this.lastName;
     }

     isAdult() {
       return this.age > 36 && this.age < 60;
     }
   }

   @Entry
   @Component
   struct parsingJSONStringsIntoInstanceObjects {
     aboutToAppear(): void {
       const instance = plainToClass(User, testJSON);
       console.info('instance:' + JSON.stringify(instance))
     }

     build() {

     }
   }
   ```
