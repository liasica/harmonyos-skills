---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-68
title: 应用闪退-ArkTS运行时崩溃（JsCrash）异常全集与定位
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用闪退-ArkTS运行时崩溃（JsCrash）异常全集与定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d94eeb0d35508d56cfa469ed7f664aeae42604a50c5e754c26ea1a794cf4911c
---

## 问题现象

应用在运行过程中突然退出（闪退），或者界面卡死后强制关闭。在开发工具的日志中可以看到明确的崩溃堆栈。此类问题通常由代码逻辑错误、语法不规范或资源操作不当引起。

以下是一段最小化的.ets代码，通过访问undefined对象的属性来触发典型的TypeError类型JsCrash：

```ts
// 文件名：JsCrashDemo.ets
@Entry
@Component
struct JsCrashDemo {
  @State message: string = '点击触发崩溃';

  build() {
    Row() {
      Column() {
        Button(this.message)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 模拟场景：尝试读取undefined变量的属性
            let emptyVar: object | undefined = undefined;
            // 下一行代码将抛出TypeError:Cannot read property 'x' of undefined
            console.info(emptyVar.x);
          })
          .width('100%')
          .height(50)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 背景知识

JsCrash是指HarmonyOS应用中的ArkTS引擎在执行代码时遇到了无法处理的异常，导致虚拟机停止运行。

系统会将崩溃时的详细信息记录在**FaultLog**中，路径通常为/data/log/faultlog/faultlogger/，文件名前缀为jscrash-。

该日志包含了崩溃类型（Exception Name）、错误信息（Message）以及完整的调用堆栈（Stacktrace），是定位问题的核心依据。

## 问题定位

定位JsCrash主要依靠系统生成的故障日志，具体步骤如下：

1. **确认崩溃发生时间（HiLog）**。

   连接设备，使用DevEco Studio的Log面板或HiLog文件。当应用闪退时：

   * **输入**：日志搜索关键词PROCESS\_KILL。
   * **输出**：找到类似ProcessManager: PROCESS\_KILL: com.example.app ... reason: JsError的日志，确认崩溃发生的时间点。
2. **提取详细堆栈（FaultLog）**。
   * 方式一：通过DevEco Studio获取日志。DevEco Studio会收集设备/data/log/faultlog/faultlogger/路径下的进程崩溃故障日志到FaultLog中，根据进程名、故障和时间分类显示。获取日志的方法参见：[FaultLog](../harmonyos-guides/ide-fault-log.md)。
   * 方式二：通过hdc获取日志，需打开开发者选项。在开发者选项打开的情况下，开发者可以通过如下命令获取日志至本地。

     ```shell
     hdc file recv /data/log/faultlog/faultlogger 本地路径
     ```

     故障日志文件名格式为：jscrash-进程名-进程UID-毫秒级时间.log。
3. **分析异常类型**。

   JS Crash的故障日志核心在于Stacktrace字段。根据应用运行阶段和编译状态的不同，堆栈信息通常呈现为以下三种形态。正确识别堆栈形态是还原代码现场的关键。

   * **场景一：标准JS调用栈（可直接跳转）**

     日志中包含了完整的SourceMap映射信息，能够直接指向源码文件（.ets）。

     + **日志特征**：
       - 文件路径清晰，通常为entry/src/main/ets/...。
       - 没有关于SourceMap的报错提示。

       **示例**：

       ```text
        Stacktrace:
           at anonymous entry (entry/src/main/ets/pages/Index.ets:18:11)
       ```
     + **分析与处理**：
       - **第一现场**：栈顶（第一行）即为崩溃发生的具体代码行。
       - **工具支持**：在DevEco Studio的Log面板或FaultLog界面中，该路径通常显示为**超链接**，点击即可直接跳转到编辑器中的对应源码位置。
   * **场景二：Raw Stack（SourceMap映射失败）**

     当系统无法获取或解析SourceMap时，日志将展示编译后的产物代码（通常是转译后的.ts或字节码偏移量），而非源码。

     + **日志特征**：
       - 出现关键词：Cannot get SourceMap info, dump raw stack或SourceMap is not initialized yet。
       - 文件路径可能指向构建中间产物（如Index.ts而非Index.ets）。
     + **常见原因**：
       1. **Cannot get SourceMap info**：SourceMap文件丢失或转换失败。
       2. **SourceMap is not initialized yet**：崩溃发生在应用启动极早阶段（如AbilityStage或OnCreate），此时系统SourceMap模块尚未初始化完毕。

       **示例**：

       ```text
        Stacktrace:
        Cannot get SourceMap info, dump raw stack:
           at anonymous (entry/src/main/ets/pages/Index.ts:49:49)
       ```
     + **分析与处理**：
       - **行号含义**：此时的行号（如49:49）对应的是编译后的构建产物，**不能**直接对应源码行号。
       - **解决方法**：需要结合构建产物中的SourceMap文件（.map）手动进行还原，或检查构建配置确保SourceMap正确生成。
   * **场景三：NAPI/Native混合栈（含异步追踪）**

     当JS代码调用Native（C++）接口（如NAPI模块）发生异常时，堆栈会呈现JS与Native混合的状态。

     + **日志特征**：
       - 栈顶可见.so动态库文件，如libark\_jsruntime.so或libace\_napi.z.so。
       - 在ARM64 Debug版本下，可能包含========SubmitterStacktrace========分隔符，用于展示异步任务的来源。**关键字段解析**：
       - **libark\_jsruntime.so**：ArkTS运行时库，负责抛出异常。
       - **libace\_napi.z.so**：NAPI层，通常是JS调用Native的边界。
       - **SubmitterStacktrace**：**异步线程栈追踪**。当崩溃发生在异步线程中，此分隔符下方的堆栈显示了**是谁（哪个主线程代码）提交了这个异步任务**。

       ```text
        Stacktrace:
        #00 pc ... /system/lib64/platformsdk/libark_jsruntime.so ... (异常抛出点)
        ...
        #06 pc ... /system/lib64/platformsdk/libace_napi.z.so(napi_throw_error+152)
        #07 pc ... /libs/arm64/libentry.so ... <- 【关键点】Native代码中抛出异常的位置
        ...
        ========SubmitterStacktrace======== <- 异步任务提交源
        #00 pc ... libuv.so(uv_queue_work+456)
        ...
        #05 at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:57:79) <- 【关键点】JS端调用Native函数的源码位置
       ```
     + **分析与处理**：
       1. 定位Native错误：查看libace\_napi.z.so下方的一帧（如示例中的libentry.so），这是业务侧C++代码报错的位置。
       2. 定位JS调用点：如果是异步调用崩溃，查看SubmitterStacktrace下方的JS栈（如示例中的#05），定位是哪段JS代码触发了这次Native调用。

## 分析结论

导致JsCrash的原因多种多样。根据日志中的**错误类型（Error name）** 和 **错误信息（Error message）**，可以将问题归纳为以下场景。

**表1** 异常处理速查表(ArkTS/JS)

| 异常类型 (Exception Type) | 错误场景/报错信息 (Message) | 问题分析 | **解决方案与代码参考** |
| --- | --- | --- | --- |
| **ArkUI状态管理与渲染** | **组件状态/渲染异常** | | |
|  | @Component xxx missing @Provide property with name xxx. Fail to resolve @Consume xxx | 子组件初始化@Consume变量时，祖先组件链中未找到同名的@Provide变量。 | 1. 检查祖先组件是否定义了@Provide('name')。  2. 确保@Consume与@Provide别名一致。  **代码：**@Provide('key') varName: string = '' |
|  | duplicate @Provide property with name xxx... @Provide override not allowed | 同名@Provide属性在父组件链中已存在，ArkUI 不允许子组件覆盖父组件的 Provide 属性。 | 1. 修改@Provide别名以避免冲突。  2. 若需修改值，请直接修改该变量而非重新定义。  **代码：**@Provide('uniqueKey') ... |
|  | ForEach id xxx: use of default id generator function not possible... | ForEach渲染复杂对象数组时，默认键值生成器失效，导致 Diff 算法异常。 | ForEach第三个参数必须显式指定键值生成函数。  **代码：**ForEach(this.arr, (item) => {...}, (item) => item.id.toString()) |
|  | Internal error. UI execution context not found(Code: 100001) | 在非 UI 上下文（如纯 TS 文件或异步回调）中调用了依赖 UI 上下文的 API（如全局router）。 | 1. 避免在非 UI 线程/上下文直接操作 UI。  2. 使用getUIContext()或WindowStage。  **代码：**uiContext.getRouter().push(...) |
| **JS/TS 运行时错误** | **类型与对象访问异常** | | |
|  | Cannot assign to read only property | 试图修改被标记为只读的属性。常见于：  1. 修改了被Object.freeze()冻结的对象属性。  2. 修改了严格模式下的只读属性。  3. 修改了底层 Native 对象映射的只读属性。 | 1. 检查属性定义，确认是否需要修改。  2. 若对象被冻结，需先克隆新对象再修改。  **代码：**let newObj = { ...readOnlyObj }; newObj.prop = val; |
|  | undefined is not iterable (cannot read property Symbol(Symbol.iterator)) | 在需要可迭代对象的场景中使用了undefined。常见于：  1.for (let x of undefined)循环。  2.[...undefined]扩展运算符。  3.const [a] = undefined数组解构。 | 1. 迭代或解构前增加判空保护。  2. 使用短路运算提供默认空数组。 |
|  | Cannot read property xxx of undefined | 变量值为undefined时尝试读取属性。 | 1. 增加判空逻辑。  **代码：**if (obj) { return obj.xxx } |
|  | xxx is not initialized | 访问了未显式初始化的变量（通常是类属性或let声明）。 | 确保类属性声明时赋值或在构造函数中初始化。  **代码：**private data: string = '' |
|  | is not callable | 试图将非函数类型的变量当作函数调用。 | 检查变量类型，确认是否被错误赋值。  **代码：**if (typeof func === 'function') func() |
|  | Receiver is not a JSObject | 调用对象方法时，this指向（Receiver）不是一个有效的 JS 对象。 | 检查call或apply的传参，或 NAPI 调用时的入参类型。 |
|  | Cannot convert a illegal value to a Primitive | 在需要原始类型（String/Number）的地方传入了无法转换的对象（如 Symbol 或特定 Object）。 | 显式调用toString()或检查数据类型转换逻辑。 |
|  | stack contains value, usually caused by circular structure | JSON.stringify或深拷贝时，对象内部存在循环引用。 | 1. 移除循环引用。  2. 使用自定义replacer函数过滤循环引用的属性。  **代码：**JSON.stringify(obj, getCircularReplacer()) |
|  | Invalid array length | 设置数组长度为负数或超出最大限制 (2^32-1)。 | 检查数组操作逻辑，避免长度计算溢出。  **代码：**if (len >= 0) arr.length = len; |
|  | Invalid parameter / The parameter invalid | API 调用时传入参数不符合规范（类型错误或取值非法）。 | 查阅 API 文档，校验入参。  **代码：**if (param !== null) api(param) |
|  | xxx（应用代码自行抛出） | 业务逻辑主动throw new Error()且未被try-catch捕获。 | 增加全局或局部的异常捕获机制。  **代码：**try { ... } catch (e) { ... } |
| **系统组件与框架** | **Web/窗口/路由/资源** |  |  |
|  | Init error. The WebviewController must be associated with a Web component | 在Web组件绑定WebviewController之前就调用了 controller 的方法。 | 确保Web({ controller: this.controller })渲染完成后再调用方法。  **代码：** 在onPageEnd或Button点击事件中调用。 |
|  | Invalid url/Syntax Error. Invalid Url string | 加载或解析的 URL 格式错误，或长度超限。 | 校验 URL 格式（协议头 http/https），进行 URL 编码。  **代码：**encodeURI(urlString) |
|  | This window state is abnormal | 尝试操作一个未创建成功或已经销毁的 Window 对象。 | 检查窗口生命周期，操作前判断窗口是否存在。 |
|  | Invalid resource ID | Unknown Resource，使用了不存在的$r('app.type.name')ID。 | 1. 检查resources目录下资源是否存在。  2.Build->Clean Project清理缓存索引。 |
|  | Session not config | 多媒体/AVSession 相关操作前未配置会话信息。 | 先调用配置接口初始化 Session。  **代码：**session.createSession(...) |
| **数据与文件系统** | **数据库/JSON/文件** |  |  |
|  | SQLite: Generic error/Already closed(14800014) | SQL 执行错误或操作已关闭的RdbStore/ResultSet。 | 1. 检查 SQL 语法。  2. 确保在close()之后不再使用对象。  3. 检查数据库是否初始化成功。 |
|  | Column out of bounds | 游标读取列索引越界（Index < 0 或 Index >= ColumnCount）。 | 检查getColumnIndex返回值及循环逻辑。  **代码：**if (idx >= 0) rs.getString(idx) |
|  | Unexpected Text in JSON: Invalid Token | JSON.parse()解析了非标准 JSON 字符串（如截断、含非法字符）。 | 捕获解析异常，打印原始字符串排查。  **代码：**try { JSON.parse(str) } catch (e) {...} |
|  | No such file or directory/Invalid relative path | 文件路径错误或文件不存在。 | 1. 使用fs.access检查存在性。  2. 使用绝对路径（Context.filesDir）。  **代码：**fs.openSync(path) |
|  | unterminated entity ref | XML/HTML 解析时遇到未转义字符（如&后未接;）。 | 对特殊字符进行转义（如&->&）。 |
| **NAPI 与 虚拟机** | **Native/内存/底层** |  |  |
|  | Can not get Prototype on non ECMA Object | NAPI 层试图获取非 JS 对象的原型，通常是指针越界或类型混乱。 | 检查 C++ 侧napi\_get\_prototype的入参合法性。 |
|  | Service exception. Possible causes... N-API invocation exception | 系统服务异常或 NAPI 状态错误，通常伴随空指针或容器异常。 | 检查 Native 代码逻辑及 IPC 通信参数。 |
|  | Stack overflow(Recursion / Allocation) | 1. 函数无限递归。  2.AllocateHugeObject分配超大内存（如 >256KB）。 | 1. 检查递归终止条件。  2. 避免一次性分配过大对象，使用流式处理。 |
|  | DecodeURI: invalid character | decodeURI或decodeURIComponent遇到非法编码序列。 | 确保字符串是合法的 UTF-8 编码序列。  **代码：**try { decodeURI(str) } catch... |
| **OOMError** | OutOfMemory when trying to allocate xxx bytes function name: Heap::AllocateHugeObject | 内存溢出 | 1. 检查是否存在内存泄漏（未清理的定时器、闭包）等。  2. 涉及图片加载时，优化大图加载，使用缩略图。 |
| **Error / System** | Failed to register custom schemes | ArkWeb 初始化时序错误。  试图在 WebView 内核已经初始化或运行之后，才去调用注册自定义协议的接口。自定义协议必须在 Web 引擎启动前（即任何 Web 组件渲染前）全局注册一次。 | 将注册代码从组件的生命周期（如aboutToAppear）移至 UIAbility的onCreate方法中。 |

## 修改建议

1. **针对TypeError（Undefined/Null）**。
   * 在访问对象属性前，进行空值判断（if (object) ...）。
   * 检查异步回调中，数据是否在UI渲染前已准备好。
2. **针对SyntaxError / ReferenceError**。
   * 检查IDE中的红色波浪线警告，这些通常是语法错误的直接提示。
   * 确保所有变量在使用前已声明并初始化，特别注意let和const的暂时性死区。
   * ArkUI状态管理（@Provide/@Consume）需严格遵循父子组件层级关系。
3. **针对OOMError**。
   * 避免在主线程加载超大图片或文件。
   * 检查代码中是否存在未清理的监听器或持续增长的数组/Map，导致内存泄漏。
4. **针对RangeError**。
   * 检查递归调用是否有终止条件，避免死循环导致栈溢出。
   * 校验数组索引访问是否越界。
5. **针对自定义Error**。
   * 涉及文件、数据库、窗口操作时，必须使用try-catch包裹代码。
   * 确保Context对象在正确的生命周期内使用，避免在组件销毁再使用Context对象。
