---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-more-cases
title: 适配指导案例
breadcrumb: 指南 > 基础入门 > 学习ArkTS语言 > 从TypeScript到ArkTS的适配指导 > 适配指导案例
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:149f52c3605db6ecb5ca1ae57ea6a89ddb185340226b13bbb7bf224a2a6cb602
---

本文通过具体应用场景中的案例，提供在ArkTS语法规则下将TS代码适配成ArkTS代码的建议。各章以ArkTS语法规则的英文名称命名，每个案例展示适配前的TS代码和适配后的ArkTS代码。

## arkts-identifiers-as-prop-names

当属性名是有效的标识符（即不包含特殊字符、空格等，并且不以数字开头），可以直接使用而无需引号。

**应用代码**

```
1. interface W {
2. bundleName: string
3. action: string
4. entities: string[]
5. }

7. let wantInfo: W = {
8. 'bundleName': 'com.huawei.hmos.browser',
9. 'action': 'ohos.want.action.viewData',
10. 'entities': ['entity.system.browsable']
11. }
```

**建议改法**

```
1. interface W {
2. bundleName: string
3. action: string
4. entities: string[]
5. }

7. let wantInfo: W = {
8. bundleName: 'com.huawei.hmos.browser',
9. action: 'ohos.want.action.viewData',
10. entities: ['entity.system.browsable']
11. }
```

## arkts-no-any-unknown

### 按照业务逻辑，将代码中的any, unknown改为具体的类型

```
1. function printObj(obj: any) {
2. console.info(obj);
3. }

5. printObj('abc'); // abc
```

**建议改法**

```
1. function printObj(obj: string) {
2. console.info(obj);
3. // ...
4. }
5. // ...
6. printObj('abc'); // abc
```

### 标注JSON.parse返回值类型

**应用代码**

```
1. class A {
2. v: number = 0
3. s: string = ''

5. foo(str: string) {
6. let tmpStr = JSON.parse(str);
7. if (tmpStr.add != undefined) {
8. this.v = tmpStr.v;
9. this.s = tmpStr.s;
10. }
11. }
12. }
```

**建议改法**

```
1. class A {
2. public v: number = 0
3. public s: string = ''

5. foo(str: string) {
6. let tmpStr: Record<string, Object> = JSON.parse(str);
7. if (tmpStr.add != undefined) {
8. this.v = tmpStr.v as number;
9. this.s = tmpStr.s as string;
10. }
11. }
12. }
```

### 使用Record类型

**应用代码**

```
1. function printProperties(obj: any) {
2. console.info(obj.name);
3. console.info(obj.value);
4. }
```

**建议改法**

```
1. function printProperties(obj: Record<string, Object>) {
2. console.info(obj.name as string);
3. console.info(obj.value as string);
4. // ...
5. }
```

## arkts-no-call-signature

使用函数类型进行替代。

**应用代码**

```
1. interface I {
2. (value: string): void;
3. }

5. function foo(fn: I) {
6. fn('abc');
7. }

9. foo((value: string) => {
10. console.info(value);
11. })
```

**建议改法**

```
1. type I = (value: string) => void

3. function foo(fn: I) {
4. fn('abc');
5. }
6. // ...
7. foo((value: string) => {
8. console.info(value);
9. // ...
10. })
```

## arkts-no-ctor-signatures-type

使用工厂函数（() => Instance）替代构造函数签名。

**应用代码**

```
1. class Controller {
2. value: string = ''

4. constructor(value: string) {
5. this.value = value;
6. }
7. }

9. type ControllerConstructor = {
10. new (value: string): Controller;
11. }

13. class testMenu {
14. controller: ControllerConstructor = Controller
15. createController() {
16. if (this.controller) {
17. return new this.controller('123');
18. }
19. return null;
20. }
21. }

23. let t = new testMenu();
24. console.info(t.createController()!.value);
```

**建议改法**

```
1. class Controller {
2. public value: string = ''

4. constructor(value: string) {
5. this.value = value;
6. }
7. }

9. type ControllerConstructor = () => Controller;

11. class TestMenu {
12. public controller: ControllerConstructor = () => {
13. return new Controller('abc');
14. }

16. createController() {
17. if (this.controller) {
18. return this.controller();
19. }
20. return null;
21. }
22. }
23. // ...
24. let t: TestMenu = new TestMenu();
25. console.info(t.createController()!.value);
```

## arkts-no-indexed-signatures

使用Record类型进行替代。

**应用代码**

```
1. function foo1(data: { [key: string]: string }) {
2. data['a'] = 'a';
3. data['b'] = 'b';
4. data['c'] = 'c';
5. }
```

**建议改法**

```
1. function foo1(data: Record<string, string>) {
2. data['a'] = 'a';
3. data['b'] = 'b';
4. data['c'] = 'c';
5. }
```

## arkts-no-typing-with-this

使用具体类型替代this。

**应用代码**

```
1. class C {
2. getInstance(): this {
3. return this;
4. }
5. }
```

**建议改法**

```
1. class C {
2. getInstance(): C {
3. return this;
4. }
5. }
```

## arkts-no-ctor-prop-decls

显式声明类属性，并在构造函数中手动赋值。

**应用代码**

```
1. class Person {
2. constructor(readonly name: string) {}

4. getName(): string {
5. return this.name;
6. }
7. }
```

**建议改法**

```
1. class Person {
2. public name: string
3. constructor(name: string) {
4. this.name = name;
5. }

7. getName(): string {
8. return this.name;
9. }
10. }
```

## arkts-no-ctor-signatures-iface

使用type定义工厂函数或普通函数类型。

**应用代码**

```
1. class Controller {
2. value: string = ''

4. constructor(value: string) {
5. this.value = value;
6. }
7. }

9. interface ControllerConstructor {
10. new (value: string): Controller;
11. }

13. class testMenu {
14. controller: ControllerConstructor = Controller
15. createController() {
16. if (this.controller) {
17. return new this.controller('abc');
18. }
19. return null;
20. }
21. }

23. let t = new testMenu();
24. console.info(t.createController()!.value);
```

**建议改法**

```
1. class Controller {
2. public value: string = ''

4. constructor(value: string) {
5. this.value = value;
6. }
7. }

9. type ControllerConstructor = () => Controller;

11. class TestMenu {
12. public controller: ControllerConstructor = () => {
13. return new Controller('abc');
14. }

16. createController() {
17. if (this.controller) {
18. return this.controller();
19. }
20. return null;
21. }
22. }

24. let t: TestMenu = new TestMenu();
25. console.info(t.createController()!.value);
```

## arkts-no-props-by-index

可以将对象转换为Record类型，以便访问其属性。

**应用代码**

```
1. function foo2(params: Object) {
2. let funNum: number = params['funNum'];
3. let target: string = params['target'];
4. }
```

**建议改法**

```
1. function foo2(params: Record<string, string | number>) {
2. let funNum: number = params['funNum'] as number;
3. let target: string = params['target'] as string;
4. }
```

## arkts-no-inferred-generic-params

所有泛型调用都应显式标注泛型参数类型，如 Map<string, T>、.map<T>()。

**应用代码**

```
1. class A {
2. str: string = ''
3. }
4. class B extends A {}
5. class C extends A {}

7. let arr: Array<A> = [];

9. let originMenusMap:Map<string, C> = new Map(arr.map(item => [item.str, (item instanceof C) ? item: null]));
```

**建议改法**

```
1. class A {
2. public str: string = ''
3. }
4. class B extends A {}
5. class C extends A {}

7. let arr: A[] = [];

9. let originMenusMap: Map<string, C | null> = new Map<string, C | null>
10. (arr.map<[string, C | null]>(item => [item.str, (item instanceof C) ? item: null]));
```

**原因**

(item instanceof C) ? item: null 需要声明类型为C | null，由于编译器无法推导出map的泛型类型参数，需要显式标注。

## arkts-no-regexp-literals

使用new RegExp(pattern, flags) 构造函数替代RegExp字面量。

**应用代码**

```
1. let regex: RegExp = /\s*/g;
```

**建议改法**

```
1. let regexp: RegExp = new RegExp('\\s*','g');
```

**原因**

如果正则表达式中使用了标志符，需要将其作为new RegExp()的参数。

## arkts-no-untyped-obj-literals

### 从SDK中导入类型，标注object literal类型

**应用代码**

```
1. const area = { // 没有写明类型 不方便维护
2. pixels: new ArrayBuffer(8),
3. offset: 0,
4. stride: 8,
5. region: { size: { height: 1,width:2 }, x: 0, y: 0 }
6. }
```

**建议改法**

```
1. import { image } from '@kit.ImageKit';
2. // ...
3. const area: image.PositionArea = { // 写明具体类型
4. pixels: new ArrayBuffer(8),
5. offset: 0,
6. stride: 8,
7. region: { size: { height: 1, width: 2 }, x: 0, y: 0 }
8. }
```

### 用class为object literal标注类型，要求class的构造函数无参数

**应用代码**

```
1. class Test {
2. value: number = 1
3. // 有构造函数
4. constructor(value: number) {
5. this.value = value;
6. }
7. }

9. let t: Test = { value: 2 };
```

**建议改法1**

```
1. // 去除构造函数
2. class Test {
3. public value: number = 1
4. }

6. let t: Test = { value: 2 };
```

**建议改法2**

```
1. // 使用new
2. class Test {
3. public value: number = 1

5. constructor(value: number) {
6. this.value = value;
7. }
8. }

10. let t: Test = new Test(2);
```

**原因**

```
1. class C {
2. value: number = 1

4. constructor(n: number) {
5. if (n < 0) {
6. throw new Error('Negative');
7. }
8. this.value = n;
9. }
10. }

12. let s: C = new C(-2);   // 抛出异常
13. let t: C = { value: -2 }; // ArkTS 不支持
```

如果允许使用C来标注object literal的类型，变量t会导致行为的二义性。ArkTS禁止通过object literal绕过这一行为。

### 用class/interface为object literal标注类型，要求使用identifier作为object literal的key

**应用代码**

```
1. class Test {
2. value: number = 0
3. }

5. let arr: Test[] = [
6. {
7. 'value': 1
8. },
9. {
10. 'value': 2
11. },
12. {
13. 'value': 3
14. }
15. ]
```

**建议改法**

```
1. class Test {
2. public value: number = 0
3. }
4. let arr: Test[] = [
5. {
6. value: 1
7. },
8. {
9. value: 2
10. },
11. {
12. value: 3
13. }
14. ]
```

### 使用Record类型为object literal标注类型，要求使用字符串作为object literal的key

**应用代码**

```
1. let obj: Record<string, number | string> = {
2. value: 123,
3. name: 'abc'
4. }
```

**建议改法**

```
1. let obj: Record<string, number | string> = {
2. 'value': 123,
3. 'name': 'abc'
4. }
```

### 函数参数类型包含index signature

**应用代码**

```
1. function foo3(obj: { [key: string]: string}): string {
2. if (obj != undefined && obj != null) {
3. return obj.value1 + obj.value2;
4. }
5. return '';
6. }
```

**建议改法**

```
1. function foo(obj: Record<string, string>): string {
2. if (obj != undefined && obj != null) {
3. return obj.value1 + obj.value2;
4. }
5. return '';
6. }
```

### 函数实参使用了object literal

**应用代码**

```
1. (fn) => {
2. fn({ value: 123, name:'' });
3. }
```

**建议改法**

```
1. class T {
2. public value: number = 0
3. public name: string = ''
4. }

6. (fn: (v: T) => void) => {
7. fn({ value: 123, name: '' });
8. }
```

### class/interface 中包含方法

**应用代码**

```
1. interface T {
2. foo(value: number): number
3. }

5. let t:T = { foo: (value) => { return value } };
```

**建议改法1**

```
1. interface T {
2. foo: (value: number) => number
3. }

5. let t:T = { foo: (value) => { return value } };
```

**建议改法2**

```
1. class T {
2. public foo: (value: number) => number = (value: number) => {
3. return value;
4. }
5. }

7. let t:T = new T();
```

**原因**

class/interface中声明的方法应被所有实例共享。ArkTS不支持通过object literal改写实例方法。ArkTS支持函数类型的属性。

### export default对象

**应用代码**

```
1. export default {
2. onCreate() {
3. // ...
4. },
5. onDestroy() {
6. // ...
7. }
8. }
```

**建议改法**

```
1. class Test {
2. onCreate() {
3. // ...
4. }
5. onDestroy() {
6. // ...
7. }
8. }

10. export default new Test()
```

### 通过导入namespace获取类型

**应用代码**

```
1. // test.d.ets
2. declare namespace test {
3. interface I {
4. id: string;
5. type: number;
6. }

8. function foo(name: string, option: I): void;
9. }

11. export default test;
```

```
1. // app.ets
2. import test from './test';

4. let option = { id: '', type: 0 };
5. test.foo('', option);
```

**建议改法**

```
1. // test.d.ets
2. declare namespace Test {
3. interface I {
4. id: string;
5. type: number;
6. }

8. function foo(name: string, option: I): void;
9. function foo(): I;
10. }

12. export default Test;
```

```
1. // app.ets
2. import test from './test';

4. let option = { id: '', type: 0 };
5. test.foo('', option);
```

**原因**

对象字面量缺少类型，根据test.foo分析可以得知，option的类型来源于声明文件，那么只需要将类型导入即可。

在test.d.ets中，I定义在namespace中。在ets文件中，先导入namespace，再通过名称获取相应的类型。

### object literal传参给Object类型

**应用代码**

```
1. function emit(event: string, ...args: Object[]): void {}

3. emit('', {
4. 'action': 11,
5. 'outers': false
6. });
```

**建议改法**

```
1. function emit(event: string, ...args: Object[]): void {}

3. let emitArg: Record<string, number | boolean> = {
4. 'action': 11,
5. 'outers': false
6. }

8. emit('', emitArg);
```

## arkts-no-obj-literals-as-types

使用interface显式定义结构类型。

**应用代码**

```
1. type Person = { name: string, age: number }
```

**建议改法**

```
1. interface Person {
2. name: string,
3. age: number
4. }
```

## arkts-no-noninferrable-arr-literals

显式声明数组元素的类型（使用interface或class），并为数组变量添加类型注解。

**应用代码**

```
1. let permissionList = [
2. { name: '设备信息', value: '用于分析设备的续航、通话、上网、SIM卡故障等' },
3. { name: '麦克风', value: '用于反馈问题单时增加语音' },
4. { name: '存储', value: '用于反馈问题单时增加本地文件附件' }
5. ]
```

**建议改法**

为对象字面量声明类型。

```
1. class PermissionItem {
2. public name?: string
3. public value?: string
4. }

6. let permissionList: PermissionItem[] = [
7. { name: '设备信息', value: '用于分析设备的续航、通话、上网、SIM卡故障等' },
8. { name: '麦克风', value: '用于反馈问题单时增加语音' },
9. { name: '存储', value: '用于反馈问题单时增加本地文件附件' }
10. ]
```

## arkts-no-method-reassignment

使用函数类型的类字段（class field）代替原型方法。

**应用代码**

```
1. class C {
2. add(left: number, right: number): number {
3. return left + right;
4. }
5. }

7. function sub(left: number, right: number): number {
8. return left - right;
9. }

11. let c1 = new C();
12. c1.add = sub;
```

**建议改法**

```
1. class C3 {
2. public add: (left: number, right: number) => number =
3. (left: number, right: number) => {
4. return left + right;
5. }
6. }

8. function sub(left: number, right: number): number {
9. return left - right;
10. }

12. let c1 = new C3();
13. c1.add = sub;
```

## arkts-no-polymorphic-unops

使用 Number.parseInt()、new Number() 等显式转换函数。

**应用代码**

```
1. let a = +'5'; // 使用操作符隐式转换
2. let b = -'5';
3. let c = ~'5';
4. let d = +'string';
```

**建议改法**

```
1. let a = Number.parseInt('5'); // 使用Number.parseInt显示转换
2. let b = -Number.parseInt('5');
3. let c = ~Number.parseInt('5');
4. let d = new Number('123');
```

## arkts-no-type-query

使用类、接口或类型别名替代typeof，避免依赖变量做类型推导。

**应用代码**

```
1. // module1.ts
2. class C {
3. value: number = 0
4. }

6. export let c = new C()
```

```
1. // module2.ts
2. import { c } from './module1'
3. let t: typeof c = { value: 123 };
```

**建议改法**

```
1. // 文件名：module1.ets
2. class C {
3. public value: number = 0
4. }

6. export { C }
```

```
1. // 文件名：module2.ets
2. import { C } from './module1'
3. let t: C = { value: 123 };
```

## arkts-no-in

### 使用Object.keys判断属性是否存在

**应用代码**

```
1. function test(str: string, obj: Record<string, Object>) {
2. return str in obj;
3. }
```

**建议改法**

```
1. function test(str: string, obj: Record<string, Object>) {
2. for (let i of Object.keys(obj)) {
3. if (i == str) {
4. return true;
5. }
6. }
7. return false;
8. }
```

## arkts-no-destruct-assignment

使用索引访问元素或手动赋值代替解构赋值。

**应用代码**

```
1. let map = new Map<string, string>([['a', 'a'], ['b', 'b']]);
2. for (let [key, value] of map) {
3. console.info(key);
4. console.info(value);
5. }
```

**建议改法**

使用数组。

```
1. let map = new Map<string, string>([['a', 'a'], ['b', 'b']]);
2. // ...
3. for (let arr of map) {
4. let key = arr[0];
5. let value = arr[1];
6. console.info(key);
7. console.info(value);
8. // ...
9. }
```

## arkts-no-types-in-catch

使用无类型 catch (error)，然后通过类型断言处理。

**应用代码**

```
1. import { BusinessError } from '@kit.BasicServicesKit'

3. try {
4. // ...
5. } catch (e: BusinessError) {
6. console.error(e.message, e.code);
7. }
```

**建议改法**

```
1. import { BusinessError } from '@kit.BasicServicesKit'
2. // ...
3. try {
4. // ...
5. } catch (error) {
6. let e: BusinessError = error as BusinessError;
7. console.error(e.message, e.code);
8. }
```

## arkts-no-for-in

使用 Object.entries(obj) + for of 替代 for in。

**应用代码**

```
1. interface Person {
2. [name: string]: string
3. }
4. let p: Person = {
5. name: 'tom',
6. age: '18'
7. };

9. for (let t in p) {
10. console.info(p[t]);  // info: "tom", "18"
11. }
```

**建议改法**

```
1. let p: Record<string, string> = {
2. 'name': 'tom',
3. 'age': '18'
4. };
5. // ...
6. for (let ele of Object.entries(p)) {
7. console.info(ele[1]); // info: "tom", "18"
8. // ...
9. }
```

## arkts-no-mapped-types

使用 Record<K, T> 替代映射类型。

**应用代码**

```
1. class C {
2. a: number = 0
3. b: number = 0
4. c: number = 0
5. }
6. type OptionsFlags = {
7. [Property in keyof C]: string
8. }
```

**建议改法**

```
1. class C {
2. public a: number = 0
3. public b: number = 0
4. public c: number = 0
5. }

7. type OptionsFlags = Record<keyof C, string>
```

## arkts-limited-throw

将对象转换为Error，或创建新的Error实例抛出。

**应用代码**

```
1. import { BusinessError } from '@kit.BasicServicesKit'

3. function ThrowError(error: BusinessError) {
4. throw error;
5. }
```

**建议改法**

```
1. import { BusinessError } from '@kit.BasicServicesKit'

3. function throwError(error: BusinessError) {
4. throw error as Error;
5. }
```

**原因**

throw语句中值的类型必须为Error或者其继承类，如果继承类是一个泛型，会有编译期报错。建议使用as将类型转换为Error。

## arkts-no-standalone-this

### 函数内使用this

**应用代码**

```
1. function foo4() {
2. console.info(this.value);
3. }

5. let obj = { value: 'abc' };
6. foo.apply(obj);
```

**建议改法1**

使用类的方法实现,如果该方法被多个类使用,可以考虑采用继承的机制。

```
1. class Test {
2. public value: string = ''
3. constructor (value: string) {
4. this.value = value
5. }

7. foo() {
8. console.info(this.value);
9. // ...
10. }
11. }

13. let obj: Test = new Test('abc');
14. obj.foo();
```

**建议改法2**

将this作为参数传入。

```
1. function foo3(obj: Test) {
2. console.info(obj.value);
3. // ...
4. }
5. // ...
6. class Test {
7. public value: string = ''
8. }
9. let obj1: Test = { value: 'abc' };
10. foo3(obj1);
```

**建议改法3**

将属性作为参数传入。

```
1. function foo5(value: string) {
2. console.info(value);
3. }

5. class Test1 {
6. value: string = ''
7. }

9. let obj2: Test1 = { value: 'abc' };
10. foo5(obj2.value);
```

### class的静态方法内使用this

**应用代码**

```
1. class Test {
2. static value: number = 123
3. static foo(): number {
4. return this.value
5. }
6. }
```

**建议改法**

```
1. class Test {
2. public static value: number = 123
3. public static foo(): number {
4. return Test.value
5. }
6. }
```

## arkts-no-spread

使用Object.assign()、手动赋值或数组方法替代扩展运算符。

**应用代码**

```
1. // test.d.ets
2. declare namespace test {
3. interface I {
4. id: string;
5. type: number;
6. }

8. function foo(): I;
9. }

11. export default test

13. // app.ets
14. import test from 'test';

16. let t: test.I = {
17. ...test.foo(),
18. type: 0
19. }
```

**建议改法**

```
1. // test.d.ets
2. declare namespace Test {
3. interface I {
4. id: string;
5. type: number;
6. }

8. function foo(name: string, option: I): void;
9. function foo(): I;
10. }

12. export default Test;
```

```
1. // app.ets
2. import test from './test';

4. let t: test.I = test.foo();
5. t.type = 0;
```

**原因**

ArkTS中，对象布局在编译期是确定的。如果需要将一个对象的所有属性展开赋值给另一个对象可以通过逐个属性赋值语句完成。在本例中，需要展开的对象和赋值的目标对象类型恰好相同，可以通过改变该对象属性的方式重构代码。

## arkts-no-ctor-signatures-funcs

在class内声明属性，而不是在构造函数上。

**应用代码**

```
1. class Controller {
2. value: string = ''
3. constructor(value: string) {
4. this.value = value
5. }
6. }

8. type ControllerConstructor = new (value: string) => Controller;

10. class testMenu {
11. controller: ControllerConstructor = Controller
12. createController() {
13. if (this.controller) {
14. return new this.controller('abc');
15. }
16. return null;
17. }
18. }

20. let t = new testMenu()
21. console.info(t.createController()!.value)
```

**建议改法**

```
1. class Controller {
2. public value: string = ''
3. constructor(value: string) {
4. this.value = value;
5. }
6. }

8. type ControllerConstructor = () => Controller;

10. class TestMenu {
11. public controller: ControllerConstructor = () => { return new Controller('abc') }
12. createController() {
13. if (this.controller) {
14. return this.controller();
15. }
16. return null;
17. }
18. }

20. let t: TestMenu = new TestMenu();
21. console.info(t.createController()!.value);
```

## arkts-no-globalthis

ArkTS不支持globalThis。一方面无法为globalThis添加静态类型，只能通过查找方式访问其属性，导致额外性能开销。另一方面，无法为globalThis的属性标记类型，无法保证操作的安全性和高性能。

说明

1. 建议按照业务逻辑根据import/export语法实现数据在不同模块的传递。
2. 必要情况下，可以通过构造的**单例对象**来实现全局对象的功能。（不能在har中定义单例对象，har在打包时会在不同的hap中打包两份，无法实现单例。）

**构造单例对象**

```
1. // 构造单例对象
2. export class GlobalContext {
3. private constructor() {}
4. private static instance: GlobalContext;
5. private _objects = new Map<string, Object>();

7. public static getContext(): GlobalContext {
8. if (!GlobalContext.instance) {
9. GlobalContext.instance = new GlobalContext();
10. }
11. return GlobalContext.instance;
12. }

14. getObject(value: string): Object | undefined {
15. return this._objects.get(value);
16. }

18. setObject(key: string, objectClass: Object): void {
19. this._objects.set(key, objectClass);
20. }
21. }
```

**应用代码**

```
1. // file1.ts

3. export class Test {
4. value: string = '';
5. foo(): void {
6. globalThis.value = this.value;
7. }
8. }
```

```
1. // file2.ts

3. globalThis.value;
```

**建议改法**

```
1. // file1.ets

3. import { GlobalContext } from './GlobalContext'

5. export class Test {
6. public value: string = '';
7. foo(): void {
8. GlobalContext.getContext().setObject('value', this.value);
9. }
10. }
```

```
1. // file2.ets

3. import { GlobalContext } from './GlobalContext'

5. GlobalContext.getContext().getObject('value');
```

## arkts-no-func-apply-bind-call

### 使用标准库中接口

**应用代码**

```
1. let arr: number[] = [1, 2, 3, 4];
2. let str = String.fromCharCode.apply(null, Array.from(arr));
```

**建议改法**

```
1. let arr: number[] = [1, 2, 3, 4];
2. let str = String.fromCharCode(...Array.from(arr));
```

### bind定义方法

**应用代码**

```
1. class A {
2. value: string = ''
3. foo: Function = () => {}
4. }

6. class Test {
7. value: string = '1234'
8. obj: A = {
9. value: this.value,
10. foo: this.foo.bind(this)
11. }

13. foo() {
14. console.info(this.value);
15. }
16. }
```

**建议改法1**

```
1. class A {
2. public value: string = ''
3. public foo: Function = () => {}
4. }

6. class Test {
7. public value: string = '1234'
8. public obj: A = {
9. value: this.value,
10. foo: (): void => this.foo()
11. }

13. foo() {
14. console.info(this.value);
15. }
16. }
```

**建议改法2**

```
1. class A {
2. public value: string = ''
3. public foo: Function = () => {}
4. }

6. class Test {
7. public value: string = '1234'
8. public foo: () => void = () => {
9. console.info(this.value);
10. }
11. public obj: A = {
12. value: this.value,
13. foo: this.foo
14. }
15. }
```

### 使用apply

**应用代码**

```
1. class A {
2. value: string;
3. constructor (value: string) {
4. this.value = value;
5. }

7. foo() {
8. console.info(this.value);
9. }
10. }

12. let a1 = new A('1');
13. let a2 = new A('2');

15. a1.foo();
16. a1.foo.apply(a2);
```

**建议改法**

```
1. class A {
2. public value: string;
3. constructor (value: string) {
4. this.value = value;
5. }

7. foo() {
8. this.fooApply(this);
9. }

11. fooApply(a: A) {
12. console.info(a.value);
13. // ...
14. }
15. }

17. let a1 = new A('1');
18. let a2 = new A('2');

20. a1.foo();
21. a1.fooApply(a2);
```

## arkts-limited-stdlib

### Object.fromEntries()

**应用代码**

```
1. let entries = new Map([
2. ['foo', 123],
3. ['bar', 456]
4. ]);

6. let obj = Object.fromEntries(entries);
```

**建议改法**

```
1. let entries = new Map([
2. ['foo', 123],
3. ['bar', 456]
4. ]);

6. let obj: Record<string, Object> = {};
7. entries.forEach((value, key) => {
8. if (key != undefined && key != null) {
9. obj[key] = value;
10. }
11. })
```

## 严格模式检查(StrictModeError)

### strictPropertyInitialization

**应用代码**

```
1. interface I {
2. name:string
3. }

5. class A {}

7. class Test {
8. a: number;
9. b: string;
10. c: boolean;
11. d: I;
12. e: A;
13. }
```

**建议改法**

```
1. {
2. interface I {
3. name:string
4. }

6. class A {}

8. class Test {
9. public a: number;
10. public b: string;
11. public c: boolean;
12. public d: I = { name:'abc' };
13. public e: A | null = null;
14. constructor(a:number, b:string, c:boolean) {
15. this.a = a;
16. this.b = b;
17. this.c = c;
18. }
19. }
20. }
```

### Type \*\*\* | null is not assignable to type \*\*\*

**应用代码**

```
1. class A {
2. bar() {}
3. }
4. function foo(n: number) {
5. if (n === 0) {
6. return null;
7. }
8. return new A();
9. }
10. function getNumber() {
11. return 5;
12. }
13. let a:A = foo(getNumber());
14. a.bar();
```

**建议改法**

```
1. class A {
2. bar() {}
3. }
4. function foo(n: number) {
5. if (n === 0) {
6. return null;
7. }
8. return new A();
9. }
10. function getNumber() {
11. return 5;
12. }

14. let a: A | null = foo(getNumber());
15. a?.bar();
```

### 严格属性初始化检查

在class中，如果一个属性没有初始化，且没有在构造函数中被赋值，ArkTS将报错。

**建议改法**

1.一般情况下，**建议按照业务逻辑**在声明时初始化属性，或者在构造函数中为属性赋值。如：

```
1. // code with error
2. class Test {
3. value: number
4. flag: boolean
5. }

7. // 方式一，在声明时初始化
8. class Test {
9. value: number = 0
10. flag: boolean = false
11. }

13. // 方式二，在构造函数中赋值
14. class Test {
15. value: number
16. flag: boolean
17. constructor(value: number, flag: boolean) {
18. this.value = value;
19. this.flag = flag;
20. }
21. }
```

2.对于对象类型（包括函数类型）A，如果不确定如何初始化，建议按照以下方式之一进行初始化：

​ 方式(i) prop: A | null = null

​ 方式(ii) prop?: A

​ 方式三(iii) prop： A | undefined = undefined

* 从性能角度看，null类型仅用于编译期的类型检查，不会影响虚拟机性能。而undefined | A被视为联合类型，运行时可能产生额外开销。
* 从代码可读性、简洁性的角度来说，prop?:A是prop： A | undefined = undefined的语法糖，**推荐使用可选属性的写法**。

### 严格函数类型检查

**应用代码**

```
1. function foo(fn: (value?: string) => void, value: string): void {}

3. foo((value: string) => {}, ''); // error
```

**建议改法**

```
1. function foo1(fn: (value?: string) => void, value: string): void {}

3. foo1((value?: string) => {}, '');
```

**原因**

例如，在以下的例子中，如果编译期不开启严格函数类型的检查，那么该段代码可以编译通过，但是在运行时会产生非预期的行为。具体来看，在foo的函数体中，一个undefined被传入fn（这是可以的，因为fn可以接受undefined），但是在代码第6行foo的调用点，传入的(value: string) => { console.info(value.toUpperCase()) }的函数实现中，始终将参数value当做string类型，允许其调用toUpperCase方法。如果不开启严格函数类型的检查，那么这段代码在运行时，会出现在undefined上无法找到属性的错误。

```
1. function foo(fn: (value?: string) => void, value: string): void {
2. let v: string | undefined = undefined;
3. fn(v);
4. }

6. foo((value: string) => { console.info(value.toUpperCase()) }, ''); // Cannot read properties of undefined (reading 'toUpperCase')
```

为了避免运行时的非预期行为，开启严格类型检查时，这段代码将无法编译通过，需要提醒开发者修改代码，确保程序安全。

### 严格空值检查

**应用代码**

```
1. class Test {
2. private value?: string;

4. public printValue () {
5. console.info(this.value.toLowerCase());
6. }
7. }

9. let t = new Test();
10. t.printValue();
```

**应用代码运行时错误原因**

编译期不开启严格空值检查，应用代码可以通过编译，但是在运行时会报错。

因为t的属性value为undefined，在调用printValue方法时，由于在该方法内未对this.value的值进行空值检查，直接按照string类型访问其属性，导致了运行时的错误。

**建议改法**

在编写代码时，建议减少可空类型的使用。如果对变量、属性标记了可空类型，那么在使用它们之前，需要进行空值的判断，根据是否为空值处理不同的逻辑。

```
1. class Test {
2. private value?: string;

4. public printValue () {
5. if (this.value) {
6. console.info(this.value.toLowerCase());
7. }
8. }
9. }

11. let t = new Test();
12. t.printValue();
```

### 函数返回类型不匹配

**应用代码**

```
1. class Test {
2. handleClick: (action: string, externInfo?: string) => void | null = null;
3. }
```

**建议改法**

在这种写法下，函数返回类型被解析为 void | undefined，需要添加括号用来区分union类型。

```
1. class Test {
2. public handleClick: ((action: string, externInfo?: string) => void) | null = null;
3. }
```

### Type '\*\*\* | null' is not assignable to type '\*\*\*'

**应用代码**

```
1. class A {
2. value: number
3. constructor(value: number) {
4. this.value = value;
5. }
6. }

8. function foo6(v: number): A | null {
9. if (v > 0) {
10. return new A(v);
11. }
12. return null;
13. }

15. let a1: A = foo6(1);
```

**建议改法1**

修改变量a的类型：let a: A | null = foo()。

```
1. class A1 {
2. value: number
3. constructor(value: number) {
4. this.value = value;
5. }
6. }

8. function foo(v: number): A1 | null {
9. if (v > 0) {
10. return new A1(v);
11. }
12. return null;
13. }

15. let a: A1 | null = foo(123);

17. if (a != null) {
18. // 非空分支
19. } else {
20. // 处理null
21. }
```

**建议改法2**

如果确定此处调用foo一定返回非空值，可以使用非空断言!。

```
1. class A2 {
2. value: number
3. constructor(value: number) {
4. this.value = value;
5. }
6. }

8. function foo(v: number): A2 | null {
9. if (v > 0) {
10. return new A2(v);
11. }
12. return null;
13. }

15. let a: A2 = foo(123)!;
```

### Cannot invoke an object which is possibly 'undefined'

**应用代码**

```
1. interface A {
2. foo?: () => void
3. }

5. let a:A = { foo: () => {} };
6. a.foo();
```

**建议改法1**

```
1. interface A {
2. foo: () => void
3. }
4. let a: A = { foo: () => {} };
5. a.foo();
```

**建议改法2**

```
1. interface A {
2. foo?: () => void
3. }

5. let a: A = { foo: () => {} };
6. if (a.foo) {
7. a.foo();
8. }
```

**原因**

在原先代码的定义中，foo是可选属性，可能为undefined，对undefined的调用会导致报错。建议根据业务逻辑判断是否需要将foo设为可选属性。如果确实需要，那么在访问该属性后需要进行空值检查。

### Variable '\*\*\*' is used before being assigned

**应用代码**

```
1. class Test {
2. value: number = 0
3. }

5. let a: Test
6. try {
7. a = { value: 1};
8. } catch (e) {
9. a.value;
10. }
11. a.value;
```

**建议改法**

```
1. class Test {
2. public value: number = 0
3. }

5. let a: Test | null = null;
6. try {
7. a = { value:1 };
8. } catch (e) {
9. if (a) {
10. a.value;
11. }
12. }

14. if (a) {
15. a.value;
16. }
```

**原因**

对于primitive types，可以根据业务逻辑赋值，例如0，''，false。

对于对象类型，可以将其类型修改为与null的联合类型，并赋值为null。使用时需要进行非空检查。

### Function lacks ending return statement and return type does not include 'undefined'.

**应用代码**

```
1. function foo7(a: number): number {
2. if (a > 0) {
3. return a;
4. }
5. }
```

**建议改法1**

根据业务逻辑，在else分支中返回合适的数值。

**建议改法2**

```
1. function foo4(a: number): number | undefined {
2. if (a > 0) {
3. return a;
4. }
5. return
6. }
```

## arkts-strict-typing-required

删除忽略注释，为所有变量显式声明类型。

**应用代码**

```
1. // @ts-ignore
2. var a: any = 123;
```

**建议改法**

```
1. let a: number = 123;
```

**原因**

ArkTS不支持通过注释的方式绕过严格类型检查。首先将注释（// @ts-nocheck或者// @ts-ignore）删去，再根据报错信息修改其他代码。

## Importing ArkTS files to JS and TS files is not allowed

## arkts-no-tsdeps

不允许.ts、.js文件import.ets文件源码。

**建议改法**

方式1.将.ts文件的后缀修改为ets，并按ArkTS语法规则适配代码。

方式2.将.ets文件中被.ts文件依赖的代码单独抽取到.ts文件中。

## arkts-no-special-imports

改为使用普通import { ... } from '...' 导入类型。

**应用代码**

```
1. import type {A, B, C, D } from '***'
```

**建议改法**

```
1. import {A, B, C, D } from '***'
```

## arkts-no-classes-as-obj

### 使用class构造实例

**应用代码**

```
1. class Controller {
2. value: string = ''
3. constructor(value: string) {
4. this.value = value
5. }
6. }

8. interface ControllerConstructor {
9. new (value: string): Controller;
10. }

12. class TestMenu {
13. controller: ControllerConstructor = Controller
14. createController() {
15. if (this.controller) {
16. return new this.controller('abc');
17. }
18. return null;
19. }
20. }

22. let t = new TestMenu();
23. console.info(t.createController()!.value);
```

**建议改法**

```
1. class Controller {
2. public value: string = ''

4. constructor(value: string) {
5. this.value = value;
6. }
7. }

9. type ControllerConstructor = () => Controller;

11. class TestMenu {
12. public controller: ControllerConstructor = () => {
13. return new Controller('abc');
14. }

16. createController() {
17. if (this.controller) {
18. return this.controller();
19. }
20. return null;
21. }
22. }

24. let t: TestMenu = new TestMenu();
25. console.info(t.createController()!.value);
```

### 访问静态属性

**应用代码**

```
1. class C1 {
2. static value: string = 'abc'
3. }

5. class C2 {
6. static value: string = 'def'
7. }

9. function getValue(obj: any) {
10. return obj['value'];
11. }

13. console.info(getValue(C1));
14. console.info(getValue(C2));
```

**建议改法**

```
1. class C1 {
2. public static value: string = 'abc'
3. }

5. class C2 {
6. public static value: string = 'def'
7. }

9. function getC1Value(): string {
10. return C1.value;
11. }

13. function getC2Value(): string {
14. return C2.value;
15. }

17. console.info(getC1Value());
18. console.info(getC2Value());
```

## arkts-no-side-effects-imports

改用动态import。

**应用代码**

```
1. import 'module'
```

**建议改法**

```
1. import('module')
```

## arkts-no-func-props

使用class来组织多个相关函数。

**应用代码**

```
1. function foo8(value: number): void {
2. console.info(value.toString());
3. }

5. foo8.add = (left: number, right: number) => {
6. return left + right;
7. }

9. foo8.sub = (left: number, right: number) => {
10. return left - right;
11. }
```

**建议改法**

```
1. class Foo {
2. static foo(value: number): void {
3. console.info(value.toString());
4. // ...
5. }

7. static add(left: number, right: number): number {
8. return left + right;
9. }

11. static sub(left: number, right: number): number {
12. return left - right;
13. }
14. }
```

## arkts-limited-esobj

使用具体类型（如number, string）或接口代替不明确的ESObject。

**应用代码**

```
1. // testa.ts
2. export function foo(): any {
3. return null;
4. }
```

```
1. // main.ets
2. import {foo} from './testa'
3. let e0: ESObject = foo();

5. function f() {
6. let e1 = foo();
7. let e2: ESObject = 1;
8. let e3: ESObject = {};
9. let e4: ESObject = '';
10. }
```

**建议改法**

```
1. // testa.ts
2. export function foo(): any {
3. return null;
4. }
```

```
1. // main.ets
2. import {foo} from './testa'
3. interface I {}

5. function f() {
6. let e0: ESObject = foo();
7. let e1: ESObject = foo();
8. let e2: number = 1;
9. let e3: I = {};
10. let e4: string = '';
11. }
```

## 拷贝

### 浅拷贝

**TypeScript**

```
1. function shallowCopy(obj: object): object {
2. let newObj = {};
3. Object.assign(newObj, obj);
4. return newObj;
5. }
```

**ArkTS**

```
1. function shallowCopy(obj: object): object {
2. let newObj: Record<string, Object> = {};
3. for (let key of Object.keys(obj)) {
4. newObj[key] = obj[key];
5. }
6. return newObj;
7. }
```

### 深拷贝

**TypeScript**

```
1. function deepCopy(obj: object): object {
2. let newObj = Array.isArray(obj) ? [] : {};
3. for (let key in obj) {
4. if (typeof obj[key] === 'object') {
5. newObj[key] = deepCopy(obj[key]);
6. } else {
7. newObj[key] = obj[key];
8. }
9. }
10. return newObj;
11. }
```

**ArkTS**

```
1. function deepCopy(obj: object): object {
2. let newObj: Record<string, Object> | Object[] = Array.isArray(obj) ? [] : {};
3. for (let key of Object.keys(obj)) {
4. if (typeof obj[key] === 'object') {
5. newObj[key] = deepCopy(obj[key]);
6. } else {
7. newObj[key] = obj[key];
8. }
9. }
10. return newObj;
11. }
```
