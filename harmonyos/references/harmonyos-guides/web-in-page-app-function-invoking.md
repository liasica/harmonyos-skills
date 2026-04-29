---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-in-page-app-function-invoking
title: 前端页面调用应用侧函数
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 在应用中使用前端页面JavaScript > 前端页面调用应用侧函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:068e621870d094de11ffac5cadd86d7172d417a7f6d8d75456d38e297226284a
---

开发者使用Web组件将应用侧代码注册到前端页面中，注册完成之后，前端页面中使用注册的对象名称就可以调用应用侧的方法。

## 如何建立应用侧与H5侧的交互通道

注册应用侧代码有两种方式，一种在Web组件初始化调用，使用[javaScriptProxy()](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)接口。另外一种在Web组件初始化完成后调用，使用[registerJavaScriptProxy()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)接口。两种方式都需要和[deleteJavaScriptRegister](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#deletejavascriptregister)接口配合使用，防止内存泄漏。

在下面的示例中，将test()方法注册在前端页面中， 该函数可以在前端页面触发运行。

应用侧使用[javaScriptProxy()](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)接口注册示例：

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class TestClass {
5. constructor() {
6. }

8. test(): string {
9. return 'ArkTS Hello World!';
10. }
11. }

13. @Entry
14. @Component
15. struct WebComponent {
16. webviewController: webview.WebviewController = new webview.WebviewController();
17. // 声明需要注册的对象
18. @State testObj: TestClass = new TestClass();

20. build() {
21. Column() {
22. Button('deleteJavaScriptRegister')
23. .onClick(() => {
24. try {
25. this.webviewController.deleteJavaScriptRegister('testObjName');
26. this.webviewController.refresh();
27. } catch (error) {
28. console.error(
29. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
30. }
31. })
32. // Web组件加载本地index.html页面
33. Web({ src: $rawfile('index1.html'), controller: this.webviewController})
34. // 将对象注入到web端
35. .javaScriptProxy({
36. object: this.testObj,
37. name: 'testObjName',
38. methodList: ['test'],
39. controller: this.webviewController,
40. // 可选参数
41. asyncMethodList: [],
42. permission: '{"javascriptProxyPermission":{"urlPermissionList":' +
43. '[{"scheme":"resource","host":"rawfile","port":"","path":""},' +
44. '{"scheme":"e","host":"f","port":"g","path":"h"}],"methodList":' +
45. '[{"methodName":"test","urlPermissionList":' +
46. '[{"scheme":"https","host":"xxx.com","port":"","path":""},' +
47. '{"scheme":"resource","host":"rawfile","port":"","path":""}]},' +
48. '{"methodName":"test11","urlPermissionList":' +
49. '[{"scheme":"q","host":"r","port":"","path":"t"},' +
50. '{"scheme":"u","host":"v","port":"","path":""}]}]}}'
51. })
52. }
53. }
54. }
```

[JavaScriptProxy.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseFrontendJSApp/entry2/src/main/ets/pages/JavaScriptProxy.ets#L16-L71)

应用侧使用[registerJavaScriptProxy()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)接口注册。

说明

* 使用[registerJavaScriptProxy()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)方法注册后，在下次加载或者重新加载后生效。

* 示例1：

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. class TestClass {
  5. constructor() {
  6. }

  8. test(): string {
  9. return 'ArkUI Web Component';
  10. }

  12. toString(): void {
  13. console.info('Web Component toString');
  14. }
  15. }

  17. @Entry
  18. @Component
  19. struct Index {
  20. webviewController: webview.WebviewController = new webview.WebviewController();
  21. @State testObj: TestClass = new TestClass();

  23. build() {
  24. Column() {
  25. // jsb对象不再使用后，需解除注册，防止内存泄漏
  26. Button('deleteJavaScriptRegister')
  27. .onClick(() => {
  28. try {
  29. this.webviewController.deleteJavaScriptRegister('testObjName');
  30. this.webviewController.refresh();
  31. } catch (error) {
  32. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  33. }
  34. })
  35. Web({ src: $rawfile('index1.html'), controller: this.webviewController })
  36. .onControllerAttached(()=>{
  37. try {
  38. this.webviewController.registerJavaScriptProxy(this.testObj, 'testObjName', ['test', 'toString'],
  39. // 可选参数, asyncMethodList
  40. [],
  41. // 可选参数, permission
  42. '{"javascriptProxyPermission":{"urlPermissionList":[{"scheme":"resource","host":"rawfile","port":"","path":""},' +
  43. '{"scheme":"e","host":"f","port":"g","path":"h"}],"methodList":[{"methodName":"test","urlPermissionList":' +
  44. '[{"scheme":"https","host":"xxx.com","port":"","path":""},{"scheme":"resource","host":"rawfile","port":"","path":""}]},' +
  45. '{"methodName":"test11","urlPermissionList":[{"scheme":"q","host":"r","port":"","path":"t"},' +
  46. '{"scheme":"u","host":"v","port":"","path":""}]}]}}'
  47. );
  48. } catch (error) {
  49. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  50. }
  51. })
  52. }
  53. }
  54. }
  ```
* 示例2：

  ```
  1. // xxx.ets
  2. // xxx.ets
  3. import { webview } from '@kit.ArkWeb';
  4. import { BusinessError } from '@kit.BasicServicesKit';

  6. class TestClass {
  7. constructor() {
  8. }

  10. test(): string {
  11. return 'ArkUI Web Component';
  12. }

  14. toString(): void {
  15. console.info('Web Component toString');
  16. }
  17. }

  19. @Entry
  20. @Component
  21. struct Index {
  22. webviewController: webview.WebviewController = new webview.WebviewController();
  23. @State testObj: TestClass = new TestClass();
  24. @State isRegistered: boolean = false;

  26. build() {
  27. Column() {
  28. // jsb对象不再使用后，需解除注册，防止内存泄漏
  29. Button('deleteJavaScriptRegister')
  30. .onClick(() => {
  31. try {
  32. this.webviewController.deleteJavaScriptRegister('testObjName');
  33. this.webviewController.refresh();
  34. } catch (error) {
  35. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  36. }
  37. })
  38. Web({ src: $rawfile('index1.html'), controller: this.webviewController })
  39. .onPageEnd(()=>{
  40. try {
  41. if(!this.isRegistered){
  42. this.webviewController.registerJavaScriptProxy(this.testObj, 'testObjName', ['test', 'toString'],
  43. // 可选参数, asyncMethodList
  44. [],
  45. // 可选参数, permission
  46. '{"javascriptProxyPermission":{"urlPermissionList":[{"scheme":"resource","host":"rawfile","port":"","path":""},' +
  47. '{"scheme":"e","host":"f","port":"g","path":"h"}],"methodList":[{"methodName":"test","urlPermissionList":' +
  48. '[{"scheme":"https","host":"xxx.com","port":"","path":""},{"scheme":"resource","host":"rawfile","port":"","path":""}]},' +
  49. '{"methodName":"test11","urlPermissionList":[{"scheme":"q","host":"r","port":"","path":"t"},' +
  50. '{"scheme":"u","host":"v","port":"","path":""}]}]}}'
  51. );
  52. this.isRegistered = true;
  53. // onPageEnd中注册方法后，需重新加载后生效
  54. this.webviewController.refresh();
  55. }
  56. } catch (error) {
  57. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  58. }
  59. })
  60. }
  61. }
  62. }
  ```
* 可选参数permission是一个JSON字符串，示例如下：

  ```
  1. {
  2. "javascriptProxyPermission": {
  3. "urlPermissionList": [       // Object级权限，如果匹配，所有Method都授权
  4. {
  5. "scheme": "resource",    // 精确匹配，不能为空，必填
  6. "host": "rawfile",       // 精确匹配，不能为空，必填
  7. "port": "",              // 精确匹配，为空不检查，必填
  8. "path": ""               // 前缀匹配，为空不检查，必填
  9. },
  10. {
  11. "scheme": "https",       // 精确匹配，不能为空，必填
  12. "host": "xxx.com",       // 精确匹配，不能为空，必填
  13. "port": "8080",          // 精确匹配，为空不检查，必填
  14. "path": "a/b/c"          // 前缀匹配，为空不检查，必填
  15. }
  16. ],
  17. "methodList": [
  18. {
  19. "methodName": "test",
  20. "urlPermissionList": [   // Method级权限
  21. {
  22. "scheme": "https",   // 精确匹配，不能为空，必填
  23. "host": "xxx.com",   // 精确匹配，不能为空，必填
  24. "port": "",          // 精确匹配，为空不检查，必填
  25. "path": ""           // 前缀匹配，为空不检查，必填
  26. },
  27. {
  28. "scheme": "resource",// 精确匹配，不能为空，必填
  29. "host": "rawfile",   // 精确匹配，不能为空，必填
  30. "port": "",          // 精确匹配，为空不检查，必填
  31. "path": ""           // 前缀匹配，为空不检查，必填
  32. }
  33. ]
  34. },
  35. {
  36. "methodName": "test11",
  37. "urlPermissionList": [   // Method级权限
  38. {
  39. "scheme": "q",       // 精确匹配，不能为空，必填
  40. "host": "r",         // 精确匹配，不能为空，必填
  41. "port": "",          // 精确匹配，为空不检查，必填
  42. "path": "t"          // 前缀匹配，为空不检查，必填
  43. },
  44. {
  45. "scheme": "u",       // 精确匹配，不能为空，必填
  46. "host": "v",         // 精确匹配，不能为空，必填
  47. "port": "",          // 精确匹配，为空不检查，必填
  48. "path": ""           // 前缀匹配，为空不检查，必填
  49. }
  50. ]
  51. }
  52. ]
  53. }
  54. }
  ```
* index1.html前端页面触发应用侧代码。

  ```
  1. <!-- index1.html -->
  2. <!DOCTYPE html>
  3. <html>
  4. <body>
  5. <button type="button" onclick="callArkTS()">Click Me!</button>
  6. <p id="demo"></p>
  7. <script>
  8. function callArkTS() {
  9. let str = testObjName.test();
  10. document.getElementById("demo").innerHTML = str;
  11. console.info('ArkTS Hello World! :' + str);
  12. }
  13. </script>
  14. </body>
  15. </html>
  ```

## 复杂类型使用方法

### 应用侧和前端页面之间传递Array

Array可以作为注册对象方法的参数或返回值，在应用侧和前端页面之间传递。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestClass {
6. constructor() {
7. }

9. test(): Array<number> {
10. return [1, 2, 3, 4]
11. }

13. toString(param: string): void {
14. console.info('Web Component toString' + param);
15. }
16. }

18. @Entry
19. @Component
20. struct Index {
21. webviewController: webview.WebviewController = new webview.WebviewController();
22. @State testObj: TestClass = new TestClass();

24. build() {
25. Column() {
26. Button('refresh')
27. .onClick(() => {
28. try {
29. this.webviewController.refresh();
30. } catch (error) {
31. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. })
34. Button('Register JavaScript To Window')
35. .onClick(() => {
36. try {
37. this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
38. } catch (error) {
39. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
40. }
41. })
42. Button('deleteJavaScriptRegister')
43. .onClick(() => {
44. try {
45. this.webviewController.deleteJavaScriptRegister("testObjName");
46. } catch (error) {
47. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
48. }
49. })
50. Web({ src: $rawfile('index.html'), controller: this.webviewController })
51. }
52. }
53. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <button type="button" onclick="callArkTS()">Click Me!</button>
6. <p id="demo"></p>
7. <script>
8. function callArkTS() {
9. testObjName.toString(testObjName.test());
10. }
11. </script>
12. </body>
13. </html>
```

### 非Function等复杂类型使用

非Function等复杂类型作为注册对象方法的参数或返回值，在应用侧和前端页面之间传递。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class Student {
6. name: string = '';
7. age: string = '';
8. }

10. class TestClass {
11. constructor() {
12. }

14. // 传递的基础类型name:"jeck", age:"12"。
15. test(): Student {
16. let st: Student = { name: "jeck", age: "12" };
17. return st;
18. }

20. toString(param: ESObject): void {
21. console.info('Web Component toString' + param["name"]);
22. }
23. }

25. @Entry
26. @Component
27. struct Index {
28. webviewController: webview.WebviewController = new webview.WebviewController();
29. @State testObj: TestClass = new TestClass();

31. build() {
32. Column() {
33. Button('refresh')
34. .onClick(() => {
35. try {
36. this.webviewController.refresh();
37. } catch (error) {
38. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
39. }
40. })
41. Button('Register JavaScript To Window')
42. .onClick(() => {
43. try {
44. this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
45. } catch (error) {
46. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
47. }
48. })
49. Button('deleteJavaScriptRegister')
50. .onClick(() => {
51. try {
52. this.webviewController.deleteJavaScriptRegister("testObjName");
53. } catch (error) {
54. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
55. }
56. })
57. Web({ src: $rawfile('index.html'), controller: this.webviewController })
58. }
59. }
60. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <button type="button" onclick="callArkTS()">Click Me!</button>
6. <p id="demo"></p>
7. <script>
8. function callArkTS() {
9. testObjName.toString(testObjName.test());
10. }
11. </script>
12. </body>
13. </html>
```

### 应用侧调用前端页面的Callback

Callback可以作为注册对象方法的参数或返回值，在应用侧和前端页面之间传递。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestClass {
6. constructor() {
7. }

9. test(param: Function): void {
10. param("call callback");
11. }

13. toString(param: String): void {
14. console.info('Web Component toString' + param);
15. }
16. }

18. @Entry
19. @Component
20. struct Index {
21. webviewController: webview.WebviewController = new webview.WebviewController();
22. @State testObj: TestClass = new TestClass();

24. build() {
25. Column() {
26. Button('refresh')
27. .onClick(() => {
28. try {
29. this.webviewController.refresh();
30. } catch (error) {
31. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. })
34. Button('Register JavaScript To Window')
35. .onClick(() => {
36. try {
37. this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
38. } catch (error) {
39. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
40. }
41. })
42. Button('deleteJavaScriptRegister')
43. .onClick(() => {
44. try {
45. this.webviewController.deleteJavaScriptRegister("testObjName");
46. } catch (error) {
47. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
48. }
49. })
50. Web({ src: $rawfile('index.html'), controller: this.webviewController })
51. }
52. }
53. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <button type="button" onclick="callArkTS()">Click Me!</button>
6. <p id="demo"></p>
7. <script>
8. function callArkTS() {
9. testObjName.test(function(param){testObjName.toString(param)});
10. }
11. </script>
12. </body>
13. </html>
```

### 应用侧调用前端页面Object里的Function

前端页面Object里的Function可以作为注册对象方法的参数或返回值，在应用侧和前端页面之间传递。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestClass {
6. constructor() {
7. }

9. test(param: ESObject): void {
10. param.hello("call obj func");
11. }

13. toString(param: string): void {
14. console.info('Web Component toString' + param);
15. }
16. }

18. @Entry
19. @Component
20. struct Index {
21. webviewController: webview.WebviewController = new webview.WebviewController();
22. @State testObj: TestClass = new TestClass();

24. build() {
25. Column() {
26. Button('refresh')
27. .onClick(() => {
28. try {
29. this.webviewController.refresh();
30. } catch (error) {
31. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. })
34. Button('Register JavaScript To Window')
35. .onClick(() => {
36. try {
37. this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
38. } catch (error) {
39. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
40. }
41. })
42. Button('deleteJavaScriptRegister')
43. .onClick(() => {
44. try {
45. this.webviewController.deleteJavaScriptRegister("testObjName");
46. } catch (error) {
47. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
48. }
49. })
50. Web({ src: $rawfile('index.html'), controller: this.webviewController })
51. }
52. }
53. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <button type="button" onclick="callArkTS()">Click Me!</button>
6. <p id="demo"></p>
7. <script>
8. // 写法1
9. class Student {
10. constructor(nameList) {
11. this.methodNameListForJsProxy = nameList;
12. }

14. hello(param) {
15. testObjName.toString(param)
16. }
17. }
18. var st = new Student(["hello"])

20. // 写法2
21. //创建一个构造器，构造函数首字母大写
22. function Obj1(){
23. this.methodNameListForJsProxy=["hello"];
24. this.hello=function(param){
25. testObjName.toString(param)
26. };
27. }
28. //利用构造器，通过new关键字生成对象
29. var st1 = new Obj1();

31. function callArkTS() {
32. testObjName.test(st);
33. testObjName.test(st1);
34. }
35. </script>
36. </body>
37. </html>
```

### 前端页面调用应用侧Object里的Function

应用侧Object里的Function可以作为注册对象方法的参数或返回值，在应用侧和前端页面之间传递。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class ObjOther {
6. methodNameListForJsProxy: string[]

8. constructor(list: string[]) {
9. this.methodNameListForJsProxy = list
10. }

12. testOther(json: string): void {
13. console.info(json)
14. }
15. }

17. class TestClass {
18. ObjReturn: ObjOther

20. constructor() {
21. this.ObjReturn = new ObjOther(["testOther"]);
22. }

24. test(): ESObject {
25. return this.ObjReturn
26. }

28. toString(param: string): void {
29. console.info('Web Component toString' + param);
30. }
31. }

33. @Entry
34. @Component
35. struct Index {
36. webviewController: webview.WebviewController = new webview.WebviewController();
37. @State testObj: TestClass = new TestClass();

39. build() {
40. Column() {
41. Button('refresh')
42. .onClick(() => {
43. try {
44. this.webviewController.refresh();
45. } catch (error) {
46. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
47. }
48. })
49. Button('Register JavaScript To Window')
50. .onClick(() => {
51. try {
52. this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
53. } catch (error) {
54. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
55. }
56. })
57. Button('deleteJavaScriptRegister')
58. .onClick(() => {
59. try {
60. this.webviewController.deleteJavaScriptRegister("testObjName");
61. } catch (error) {
62. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
63. }
64. })
65. Web({ src: $rawfile('index.html'), controller: this.webviewController })
66. }
67. }
68. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <button type="button" onclick="callArkTS()">Click Me!</button>
6. <p id="demo"></p>
7. <script>
8. function callArkTS() {
9. testObjName.test().testOther("call other object func");
10. }
11. </script>
12. </body>
13. </html>
```

### Promise场景

第一种使用方法，在应用侧new Promise，将Promise作为对象方法的参数或返回值，向前端页面传递。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestClass {
6. constructor() {
7. }

9. test(): Promise<string> {
10. let p: Promise<string> = new Promise((resolve, reject) => {
11. setTimeout(() => {
12. console.info('执行完成');
13. reject('fail');
14. }, 10000);
15. });
16. return p;
17. }

19. toString(param: string): void {
20. console.info(" " + param);
21. }
22. }

24. @Entry
25. @Component
26. struct Index {
27. webviewController: webview.WebviewController = new webview.WebviewController();
28. @State testObj: TestClass = new TestClass();

30. build() {
31. Column() {
32. Button('refresh')
33. .onClick(() => {
34. try {
35. this.webviewController.refresh();
36. } catch (error) {
37. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
38. }
39. })
40. Button('Register JavaScript To Window')
41. .onClick(() => {
42. try {
43. this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
44. } catch (error) {
45. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
46. }
47. })
48. Button('deleteJavaScriptRegister')
49. .onClick(() => {
50. try {
51. this.webviewController.deleteJavaScriptRegister("testObjName");
52. } catch (error) {
53. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
54. }
55. })
56. Web({ src: $rawfile('index.html'), controller: this.webviewController })
57. }
58. }
59. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <button type="button" onclick="callArkTS()">Click Me!</button>
6. <p id="demo"></p>
7. <script>
8. function callArkTS() {
9. testObjName.test().then((param)=>{testObjName.toString(param)}).catch((param)=>{testObjName.toString(param)})
10. }
11. </script>
12. </body>
13. </html>
```

第二种使用方法，在前端页面new Promise，将Promise作为对象方法的参数或返回值，向应用侧传递。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class TestClass {
6. constructor() {
7. }

9. test(param:Function): void {
10. setTimeout( () => { param("suc") }, 10000)
11. }

13. toString(param:string): void {
14. console.info(" " + param);
15. }
16. }

18. @Entry
19. @Component
20. struct Index {
21. webviewController: webview.WebviewController = new webview.WebviewController();
22. @State testObj: TestClass = new TestClass();

24. build() {
25. Column() {
26. Button('refresh')
27. .onClick(() => {
28. try {
29. this.webviewController.refresh();
30. } catch (error) {
31. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
32. }
33. })
34. Button('Register JavaScript To Window')
35. .onClick(() => {
36. try {
37. this.webviewController.registerJavaScriptProxy(this.testObj, "testObjName", ["test", "toString"]);
38. } catch (error) {
39. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
40. }
41. })
42. Button('deleteJavaScriptRegister')
43. .onClick(() => {
44. try {
45. this.webviewController.deleteJavaScriptRegister("testObjName");
46. } catch (error) {
47. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
48. }
49. })
50. Web({ src: $rawfile('index.html'), controller: this.webviewController })
51. }
52. }
53. }
```

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <body>
5. <button type="button" onclick="callArkTS()">Click Me!</button>
6. <p id="demo"></p>
7. <script>
8. function callArkTS() {
9. let funpromise
10. var p = new Promise(function(resolve, reject){funpromise=(param)=>{resolve(param)}})
11. testObjName.test(funpromise)
12. p.then((param)=>{testObjName.toString(param)})
13. }
14. </script>
15. </body>
16. </html>
```

## 验证通道是否建立成功

1. 打开web调试。

   开启web调试请参考[使用DevTools工具调试前端页面](web-debugging-with-devtools.md)。
2. 举例说明通道是否建立成功。

   使用[复杂类型使用方法](web-in-page-app-function-invoking.md#复杂类型使用方法)中应用侧和前端页面之间传递Array作为示例，调试结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/dJHAumAvQ-GzmC8eRDU78g/zh-cn_image_0000002589244511.png?HW-CC-KV=V1&HW-CC-Date=20260429T052916Z&HW-CC-Expire=86400&HW-CC-Sign=5421D05E6405C57FFDE45C44DBD179219C1068B290F2B4FD506F6938D4F82B66)
