---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-optimizations
title: JSVM通用调优实践
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API调优&高性能使用示例 > JSVM通用调优实践
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ab00b33dc61d9924aacab34a2e26b2511b0828979e5b711aa876f8c0ea3a8224
---

## JSVM调用结构

小程序使用JSVM执行JS代码的过程可以分为 Native，JSVM-API，JSVM 三层：

* Native：小程序运行JS的逻辑层，使用JSVM提供的接口完成JS代码编译，运行，code cache生成等操作的逻辑排布和组合
* JSVM-API：连接native和v8的接口兼容层，保持对不同版本JS引擎的兼容，提供JS引擎标准化的使用实践
* JSVM：JS引擎层，负责JS代码实际的编译运行

使用JSVM的过程中，可能会因为多种原因产生不必要的开销，导致启动速度变慢。可以从以下三个层面进行分析。

## 提升启动速度

对于使用JSVM的应用启动场景，我们可以区分冷热启动用于分别进行不同的优化。

首先是冷启动，是没有任何profile或者cache可以用于优化的场景，通常是首次启动；

热启动则是已经充分预热，在多次启动之后获取了足量用于优化的cache的场景。

### 减少 JS 引擎层的开销

引擎层的开销很大程度上来源于编译。通过合理调整调用JSVM-API时传入的选项，可以降低主线程上JS引擎的编译开销。

以下面的编译接口为例，其中eagerCompile这个参数的开关可以调控编译行为，通过在不同的启动场景打开这个选项可以实现优化效果。

```
1. /**
2. * ...
3. * @param eagerCompile: Whether to compile the script eagerly.
4. * ...
5. */
6. JSVM_EXTERN JSVM_Status OH_JSVM_CompileScript(JSVM_Env env,
7. JSVM_Value script,
8. const uint8_t* cachedData,
9. size_t cacheDataLength,
10. bool eagerCompile, // 开启全量编译
11. bool* cacheRejected,
12. JSVM_Script* result);
```

同时，code cache的生成和使用也会对编译产生影响，这部分可以参考 [使用code cache加速编译](use-jsvm-about-code-cache.md)。

**热启动：生成足够多的code cache**

热启动场景下，我们会在热启动前生成code cache以减少编译带来的开销。这个时候生成的code cache的覆盖率会影响code cache对热启动的优化效果。

有一个简单的策略可以生成足够的code cache：在生成code cache之前的那次编译中，打开eager compile选项。这样，V8会在编译时进行全量编译，确保生成的code cache是全量的。

这个方法会增加额外的编译时间开销，可能影响冷启动时间。后续将详细讨论native层的冷启动优化方法。

**冷启动：使用lazy compile代替eager compile**

在冷启动时，eager compile会增加不必要的编译时间。这其中主要的原因是没有拿到v8 lazy compile优化效果：v8会将不在必经路径上的函数推迟编译，在实际运行到的时候才进行编译，这样会减少一些不被运行到函数的编译，从而优化冷启动的时间。

因此，在冷启动时，可以通过关闭eager compile选项来避免阻塞主线程，从而获得足够的冷启动优化效果。

### 在native层减少时间开销

**冷启动：减少code cache的影响**

上面在考虑减少v8层开销的时候，提到了为了热启动的性能可以开启eager compile进行编译，而为了冷启动性能却又需要关闭eager compile选项，看起来是矛盾的。为了解决这个矛盾，避免在冷热启动性能上的权衡，关键点是在code cache生成本身。

首先，生成code cache需要进行前置编译，其次，生成code cache本身也会产生开销。

在native层，要解决冷启动与生成code cache之间的矛盾，可以另起一个线程用于生成code cache，这样可以避免生成code cache操作对冷启动的影响。

有两个方法可以参考（以下伪代码仅用于展示逻辑流程，不涉及实际的API调用）：

* 将生成code cache必需的前置编译也放到新增的线程上，这样编译选项可以分开使用：生成code cache打开eager compile，冷启动运行则关闭，这样做的缺点是可能进一步提高运行时的峰值资源占用，优点是code cache生成和运行可以完全解耦，不再需要考虑生成code cache的时间点。该流程的伪代码如下所示

```
1. async_create_code_cache() {
2. compile_with_eager_compile();
3. create_code_cache();
4. save_code_cache();
5. }

9. if (has_code_cache) {
10. evaluate_script_with_code_cache();
11. } else {
12. start_thread(async_create_code_cache());
13. evaluate_script_without_code_cache();
14. }
```

* 在启动过程中的所有路径运行完之后，再启动新线程生成code cache，这样不必使用eager compile也能获取足量的code cache，同时保证热启动性能不受影响，这样做的缺点是生成code cache的时间点受限，优点是峰值资源占用相对更少，且不必生成过量的code cache导致io变慢。这个流程可以用如下所示的伪代码来表示

```
1. async_create_code_cache() {
2. compile_with_out_eager_compile();
3. create_code_cache();
4. save_code_cache();
5. }

9. if (has_code_cache) {
10. evaluate_script_with_code_cache();
11. } else {
12. evaluate_script_without_code_cache();
13. }

17. if (script_run_completed) {
18. start_thread(async_create_code_cache());
19. }
```

### 使用更高效的JSVM-API

在能达到相同效果时，使用更高效的JSVM-API是一种有效的性能优化方法，以下是一些具体的实践示例。

**使用IsXXX代替TypeOf**

过去发现，针对仅需要判断对象类型的场景，存在一种相对低效的使用方法：

从OH\_JSVM\_TypeOf接口获取类型后，再判断是否与某个类型相同。

这种方法需要先查询object的类型，这种方法相对于直接使用is方法会更慢，因此我们新增了针对基础类型的IsXXX系列方法，用更高效的接口代替了相对低效的接口。下面的示例中使用到的JSVM-API可以参考 [JSVM数据类型与接口说明](jsvm-data-types-interfaces.md)，这里仅展示调用的步骤。

* 低效用例

```
1. bool Test::IsFunction(JSVM_Env env, JSVM_Value jsvmValue) const {
2. // type judgment
3. JSVM_ValueType valueType;
4. OH_JSVM_TypeOf(*env, jsvmValue, &valueType);
5. return valueType == JSVM_FUNCTION;
6. }
```

* 高效用例

```
1. bool Test::IsFunction(JSVM_Env env, JSVM_Value jsvmValue) const {
2. // type judgment
3. bool result = false;
4. OH_JSVM_IsFunction(*env, jsvmValue, &result); // 可直接判断是否为Function类型
5. return result;
6. }
```

以某生态应用小程序场景为例，这个优化可以带来的性能收益端到端有150ms，总占比约5%。

**直接使用OH\_JSVM\_CreateReference，避免创建冗余的object**

过去存在这样一种创建reference的路径：

创建一个新的object->设置object的值->创建object的reference。

在已有值的情况下，直接创建值的引用即可。

下面的示例中使用的JSVM-API可以参考 [JSVM数据类型与接口说明](jsvm-data-types-interfaces.md)，这里仅展示调用的步骤。

* 低效用例

```
1. // (1) open handle scope
2. JSVM_HandleScope scope;
3. OH_JSVM_OpenHandleScope(*env, &scope);
4. // (2) get JSVM_Value
5. JSVM_Value jsvmValue;
6. OH_JSVM_GetNull(*env, &jsvmValue);
7. // (3) create and store Reference for JSVM_Value
8. JSVM_Value wrappingObject;
9. OH_JSVM_CreateObject(*env, &wrappingObject);
10. OH_JSVM_SetElement(*env, wrappingObject, 1, jsvmValue);
11. OH_JSVM_CreateReference(*env, wrappingObject, 1, &result->p_member->jsvmRef);
12. // (4) close handle scope
13. OH_JSVM_CloseHandleScope(*env, scope);
```

* 高效用例

```
1. // (1) open handle scope
2. JSVM_HandleScope scope;
3. OH_JSVM_OpenHandleScope(*env, &scope);
4. // (2) get JSVM_Value
5. JSVM_Value jsvmValue;
6. OH_JSVM_GetNull(*env, &jsvmValue);
7. // (3) create and store Reference for JSVM_Value
8. OH_JSVM_CreateReference(*env, jsvmValue, 1, &result->p_member->jsvmRef); // 可从任意对象类型直接创建Reference，代码更为简洁高效
9. // (4) close handle scope
10. OH_JSVM_CloseHandleScope(*env, scope);
```

同样以某生态应用小程序场景为例，这个改动减少了大量冗余的接口调用，最终带来的端到端时间收益有100+ms，约3%。
