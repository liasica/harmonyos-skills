---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-complex-type-pass
title: 跨语言调用复杂参数传递
breadcrumb: 最佳实践 > NDK开发 > 跨语言调用复杂参数传递
category: best-practices
scraped_at: 2026-04-29T14:11:48+08:00
doc_updated_at: 2026-03-26
content_hash: sha256:bed08dd650c9ba3c6dd5b1ba42f9a92b893aa4554ff7bfaa151b5a9fba59ff21
---

## 概述

开发者为了提高程序运行效率，通常需要将一些运算量较大的内容放在C++环境中运行，因此经常需要进行ArkTS与C++之间的数据传递。本文以常见的五种数据类型：Array(uint8Array)、Object、HashMap、PixelMap、Class为例，向开发者介绍如何进行复杂参数的跨语言传递。

在开始介绍不同场景的开发流程之前，请注意，跨语言数据传递，需要使用[Node-API](../harmonyos-references/napi.md)。因此，在新建项目后，请手动新建Native模块，方法如图所示:

**图1** 新建Napi模块  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/9WC7MjjsRO2BIS9aA1dM3Q/zh-cn_image_0000002229450485.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=F49A54A2A7F1BB462457DE4E1649DE5F1044C7D150C20A04ED37C9098FF3E840 "点击放大")

## 场景案例

### arrayBuffer类型数据交互

本章以简单的数组传递场景为例，在ArkTS侧输入一个Uint8Array数组，传递到C++侧，再构造另一个数组，并返回ArkTS侧。

以此为例，介绍ArrayBuffer类型的数据如何相互传递使用。除数组外，string等连续数据类型也可参考本段。

**实现原理**

ArrayBuffer是一种用于表示通用的、固定长度的原始二进制数据缓冲区的对象。在C++侧接受该类型参数时一般会通过Node-API提供的函数（如napi\_get\_arraybuffer\_info()）获取到ArrayBuffer的数据指针和长度，从而可以访问和操作这些数据。

从C++侧传递ArrayBuffer数据到ArkTS侧时，通常会在C++层创建出一个数据缓冲区（如std::vector<uint8\_t>）并填充所需的数据。然后使用Node-API提供的函数（如napi\_create\_arraybuffer()和napi\_create\_typedarray()）在ArkTS侧创建一个新的ArrayBuffer对象，并将其与C++层的数据缓冲区关联起来。最后传递该对象到ArkTS侧。

**开发步骤**

1. 需要先在index.d.ts文件中，声明一个用于数据传递的函数。

   ```
   1. export const uint8ArrayPassing: (input: Uint8Array) => Uint8Array;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/types/libentry/Index.d.ts#L20-L20)

   并在ArkTS文件中进行引用，如：

   ```
   1. import ParamPassing from 'libentry.so';
   ```

   [Uint8ArrayPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/Uint8ArrayPage.ets#L17-L17)

   使用时将Uint8Array类型的数据作为参数传入uint8ArrayPassing()函数即可。

   ```
   1. // entry/src/main/ets/pages/Uint8ArrayPage.ets
   2. paramPassing() {
   3. let sendArray: number[] = [];
   4. try {
   5. this.inputArray.forEach((inputField) => {
   6. if (inputField.inputStr.length > 0) {
   7. if (Number(inputField.inputStr) <= 0xff) {
   8. sendArray.push(Number(inputField.inputStr));
   9. } else {
   10. throw new Error('Invalid data type.');
   11. }
   12. }
   13. })
   14. this.printStr = `Array: [${ParamPassing.uint8ArrayPassing(new Uint8Array(sendArray))}]`;
   15. } catch (e) {
   16. this.printStr = e?.message;
   17. }
   18. }
   ```

   [Uint8ArrayPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/Uint8ArrayPage.ets#L49-L66)
2. 在C++工程中，定义数据传递函数。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. static napi_value Uint8ArrayPassing(napi_env env, napi_callback_info info) {
   3. vector<uint8_t> num_array = {};
   4. Uint8ArrayPassingTs2Napi(env, info, num_array);
   5. return Uint8ArrayPassingNapi2Ts(env, num_array);
   6. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L110-L115)

   其中uint8ArrayPassingTs2Napi()与uint8ArrayPassingNapi2Ts()分别负责数据从ArkTS至C++传递与反向传递。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. void Uint8ArrayPassingTs2Napi(napi_env env, napi_callback_info info, vector<uint8_t> &input_array) {
   3. // Obtain parameters transmitted from the TS layer
   4. size_t argc = 1;
   5. napi_value args;
   6. // Gets detailed information about the function call, such as input parameters.
   7. napi_get_cb_info(env, info, &argc, &args, NULL, NULL);
   8. napi_value input_array_napi = args;

   10. // Retrieve the input array typedarray and generate input_buffer
   11. napi_typedarray_type type;
   12. napi_value input_buffer;
   13. size_t byte_offset;
   14. size_t length;
   15. napi_get_typedarray_info(env, input_array_napi, &type, &length, NULL, &input_buffer, &byte_offset);

   17. // Retrieve array data
   18. void *data;
   19. size_t byte_length;
   20. napi_get_arraybuffer_info(env, input_buffer, &data, &byte_length);

   22. if (type == napi_uint8_array) {
   23. uint8_t *data_bytes = (uint8_t *)(data);
   24. int num = length / sizeof(uint8_t);

   26. for (int i = 0; i < num; i++) {
   27. input_array.push_back(*((uint8_t *)(data_bytes) + i));
   28. }
   29. }

   31. return;
   32. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L75-L106)

   在这段代码中，先用三个函数获取关键信息：

   napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

   napi\_get\_typedarray\_info()：用于在Node-API模块中获得某个TypedArray的各种属性。

   napi\_get\_arraybuffer\_info()：获取ArrayBuffer的底层数据缓冲区和长度。

   之后，通过循环配合指针和偏移量，读取其中的数据，并将其存入inputArray中。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. napi_value Uint8ArrayPassingNapi2Ts(napi_env env, vector<uint8_t> &output_array) {
   3. // Number of data
   4. int num = output_array.size();

   6. // create output_buffer
   7. napi_value output_buffer;
   8. void *output_ptr = NULL;
   9. napi_create_arraybuffer(env, num * sizeof(uint8_t), &output_ptr, &output_buffer);

   11. // output_array
   12. napi_value output_array_napi;
   13. napi_create_typedarray(env, napi_uint8_array, num, output_buffer, 0, &output_array_napi);

   15. // Assign values to output_ptr and output_buffer
   16. uint8_t *output_bytes = (uint8_t *)output_ptr;
   17. for (int i = 0; i < num; i++) {
   18. output_bytes[i] = output_array[i];
   19. }

   21. return output_array_napi;
   22. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L50-L71)

   在这段代码中，先用两个函数构建buffer和array：

   * napi\_create\_arraybuffer()：负责构建buffer。
   * napi\_create\_typedarray()：负责构建array。

   之后，通过循环，将数据压入output\_buffer，再返回output\_array，即完成了uint8Array类型数据向ArkTS的传递。
3. 在Init()函数中，实现ArkTS接口与C++接口的绑定和映射。

   ```
   1. static napi_value Init(napi_env env, napi_value exports) {
   2. napi_property_descriptor desc[] = {
   3. {"uint8ArrayPassing", nullptr, Uint8ArrayPassing, nullptr, nullptr, nullptr, napi_default, nullptr},
   4. // ...
   5. };
   6. // ...
   7. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L362-L389)

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/m04cS4yyTJG1TczQ0EFjUg/zh-cn_image_0000002194010204.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=AF2677169A28FDE2F3214E0710FDE3BE828D6556BA49B0CDA36AA663DA10BE12 "点击放大")

### object类型数据交互

本章通过模拟一个“排号机”应用，向开发者介绍如何进行object数据类型的相互传递，以及如何解析、修改其中的数据。

**实现原理**

Object类是所有其他类型的基类。在C++侧接收该类型参数时一般会通过Node-API提供的函数（如napi\_get\_named\_property()）来获取object对象的某个属性，从而操作其属性值。

从C++侧传递object类型到ArkTS侧时，可以利用Node-API封装好的接口（napi\_create\_object\_with\_named\_properties()）直接通过传递参数数组的方式构建出一个带有给定属性值的object类型对象。

**开发步骤**

1. 函数声明与调用，与[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)类同，此处不再赘述。

   特别的，此处还需定义需要使用的object数据类型。

   作为一个简单的“排号机”(比如医院中的)，需要年龄和姓名作为输入，并额外返回标志成人与否的布尔值和所排序号。因此，构造如下两种object，分别用于输入和输出。

   ```
   1. // entry/src/main/ets/model/SampleObject.ts
   2. export type SampleInputObject = {
   3. age: number;
   4. name: string;
   5. }

   7. export type SampleOutputObject = {
   8. isAdult: boolean;
   9. code: number;
   10. age: number;
   11. name: string;
   12. }
   ```

   [SampleObject.ts](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/model/SampleObject.ts#L17-L28)
2. 在C++工程中，定义数据传递函数。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. static napi_value ObjectPassing(napi_env env, napi_callback_info info) {
   3. return ObjectPassingNapi2Ts(env, ObjectPassingTs2Napi(env, info));
   4. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L166-L169)

   其中objectPassingTs2Napi()与objectPassingNapi2Ts()分别负责数据从ArkTS至C++传递与反向传递。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. napi_value ObjectPassingTs2Napi(napi_env env, napi_callback_info info) {
   3. // Obtain parameters transmitted from the TS layer
   4. size_t argc = 1;
   5. napi_value args;
   6. // Gets detailed information about the function call, such as input parameters.
   7. napi_get_cb_info(env, info, &argc, &args, NULL, NULL);

   9. return args;
   10. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L119-L128)

   napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. napi_value ObjectPassingNapi2Ts(napi_env env, napi_value inputObj) {
   3. static int32_t codeChild = 1;
   4. static int32_t codeAdult = 1;

   6. napi_value input_age;
   7. napi_value input_name;
   8. napi_get_named_property(env, inputObj, "age", &input_age);
   9. napi_get_named_property(env, inputObj, "name", &input_name);

   11. napi_value output_obj;
   12. napi_value output_is_adult;
   13. napi_value output_code;
   14. napi_value output_age = input_age;
   15. napi_value output_name = input_name;
   16. int32_t age;
   17. napi_get_value_int32(env, input_age, &age);
   18. napi_get_boolean(env, age >= 18, &output_is_adult);
   19. if (age < 18) {
   20. napi_create_int32(env, codeChild++, &output_code);
   21. } else {
   22. napi_create_int32(env, codeAdult++, &output_code);
   23. }

   25. const char *keysArray[] = {"isAdult", "code", "age", "name"};
   26. const napi_value outputArray[] = {output_is_adult, output_code, output_age, output_name};

   28. napi_create_object_with_named_properties(env, &output_obj, 4, keysArray, outputArray);

   30. return output_obj;
   31. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L132-L162)

   napi\_get\_named\_property()：负责获取并储存inputObj中的属性。

   napi\_get\_value\_int32()：负责将获取到的inputAge属性解析为int32数据，并存入age中。

   napi\_get\_boolean()：负责将需要返回的boolean属性写入对应的napi\_value量中。

   napi\_create\_int32()：负责将需要返回的int32属性写入对应的napi\_value量中。

   napi\_create\_object\_with\_named\_properties()：负责构造需要返回的object。
3. 在DevEco Studio[预生成](bpta-complex-type-pass.md#fig08576372193)的Init()函数中设置写好的数据传递函数。与[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)类同，此处不再赘述。

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/64JV31uwTAiwiIyx_y7pug/zh-cn_image_0000002194010224.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=F34B45E13360A27539D3AF55B2B7248B9ABBF293D55C554E2FC86C24AB90735C "点击放大")

### hashMap类型数据交互

本章通过模拟一个“积分累计”应用，每次输入对象的本次积分，并返回所有对象的累积积分。向开发者介绍如何进行hashMap数据类型的相互传递，以及如何解析、修改其中的数据。

**实现原理**

hashMap是一种基于哈希表的Map接口实现的数据结构。在C++侧接受该类型参数时，由于C++没有可以直接接收该类型参数的数据类型，所以一般采用两种方式进行传递。

1.传递数组：分别将HashMap的key、value作为数组取出，然后将两个数组传递至C++侧并组装成Map进行数据处理。

2.传递JSON：将HashMap转为Json字符串传递至C++侧，在C++侧通过反序列化的方式构造成Map类型数据进行处理。

同样的，从C++侧传递Map类型到ArkTS侧时，需要将Map序列化成Json字符串传递到ArkTS，然后在ArkTS侧进行反序列化获取对应参数。

**开发步骤**

1. 函数声明与调用，与[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)类同，此处不再赘述。

   此外，由于程序不支持直接传递hashMap类型，因此需要使用其他数据类型作为媒介。

   有两种主流方案：

   1. 通过JSON进行序列化和反序列化，以string类型为媒介；
   2. 将key和value拆成两个array，并以此为媒介。

   本文以前者为例，后者可参考：[如何实现ArkTS与C/C++的HashMap转换](../harmonyos-faqs/faqs-ndk-67.md)

   同时，由于ArkTS中的JSON.stringify不支持直接将hashMap序列化，因此还需将hashMap先转换为Record，再序列化。方法如下：

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. hashMap2Rec(map: HashMap<string, Object>): Record<string, Object> {
   3. let Rec: Record<string, Object> = {}

   5. try {
   6. map.forEach((value: Object, key: string) => {
   7. // value may also be HashMap
   8. if (value instanceof HashMap) {
   9. let vRec: Record<string, Object> = this.hashMap2Rec(value);
   10. value = vRec;
   11. }
   12. Rec[key] = value;
   13. })
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. hilog.error(0x0000, 'testTag', `forEach fail. code = ${err.code}, message = ${err.message}`);
   17. }

   19. return Rec;
   20. }
   ```

   [HashMapPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/HashMapPage.ets#L50-L70)

   之后，将Record类型数据通过JSON.stringify序列化后即可传入C++侧。
2. 在C++工程中，定义数据传递函数。

   ```
   1. static napi_value HashMapPassing(napi_env env, napi_callback_info info) {
   2. return HashMapPassingNapi2Ts(env, HashMapPassingTs2Napi(env, info));
   3. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L199-L201)

   其中hashMapPassingNapi2Ts()与hashMapPassingTs2Napi()分别负责数据从ArkTS至C++传递与反向传递。同时，在C++侧，也需完成序列化和反序列化，本文采用nlohmann三方库完成此操作。

   三方库获取：[OpenHarmony / third\_party\_json · GitCode](https://gitcode.net/openharmony/third_party_json)

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. map<string, int> HashMapPassingTs2Napi(napi_env env, napi_callback_info info) {
   3. size_t argc = 1;
   4. napi_value args;
   5. // Gets detailed information about the function call, such as input parameters.
   6. napi_get_cb_info(env, info, &argc, &args, nullptr, nullptr);

   8. return nlohmann::json::parse(Value2String(env, args).c_str());
   9. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L173-L181)

   napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

   value2String()：将napi\_value数据解析为string的过程包装为一个函数，方便多次调用。

   nlohmann::json::parse()：负责将string反序列化为map<string, int>类型数据。

   其中，value2String函数需要开发者自己实现。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. static std::string Value2String(napi_env env, napi_value value) {
   3. size_t string_size = 0;
   4. // Get string length
   5. napi_get_value_string_utf8(env, value, nullptr, 0, &string_size);
   6. std::string result_string;
   7. result_string.resize(string_size + 1);
   8. // Convert to string based on length
   9. napi_get_value_string_utf8(env, value, &result_string[0], string_size + 1, &string_size);
   10. return result_string;
   11. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L24-L34)

   napi\_get\_value\_string\_utf8()：负责将napi\_value数据解析为string。

   说明

   此处stringSize需要+1，这是因为napi\_value是一个C的结构体指针，C语言的字符串实际上是使用空字符 \0 结尾的一维字符数组。而napi\_get\_value\_string\_utf8返回的stringSize，其长度不含结尾的\0。为了保证写入valueString的内容包含结尾的\0，所以需要+1。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. napi_value HashMapPassingNapi2Ts(napi_env env, map<string, int> inputMap) {
   3. static map<string, int> points_table;
   4. std::map<string, int>::iterator iter;
   5. for (iter = inputMap.begin(); iter != inputMap.end(); ++iter) {
   6. points_table[iter->first] += iter->second;
   7. }

   9. string dump_string = nlohmann::ordered_json(points_table).dump();
   10. return String2value(env, dump_string);
   11. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L185-L195)

   nlohmann::ordered\_json()：负责将map序列化。

   dump()：负责将序列化后的数据转换为string类型。

   string2value()：将string转换为napi\_value的过程包装为一个函数，方便多次调用。

   其中，string2value()也需要开发者自己实现。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. static napi_value String2value(napi_env env, string str) {
   3. int length = str.length();

   5. napi_value output_string;
   6. napi_create_string_utf8(env, str.c_str(), length, &output_string);

   8. return output_string;
   9. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L38-L46)

   napi\_create\_string\_utf8()：负责将string类型数据转换为napi\_value类型。
3. 需在DevEco Studio[预生成](bpta-complex-type-pass.md#fig08576372193)的Init()函数中设置写好的数据传递函数。与[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)类同，此处不再赘述。
4. 将C++侧返回的string重新反序列化为hashMap。

   ```
   1. // entry/src/main/ets/pages/HashMapPage.ets
   2. let receiveObj: object = JSON.parse(receiveStr);
   3. let receiveMap: HashMap<string, number> = new HashMap();
   4. Object.entries(receiveObj).forEach((value: [string, number]) => {
   5. receiveMap.set(value[0], value[1]);
   6. })
   ```

   [HashMapPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/HashMapPage.ets#L87-L92)

   JSON.parse()：此函数只能将string反序列化为object，因此还需额外一步将其转换为hashMap类型。

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/vdo3f7a8RYGMQKlREfyGPA/zh-cn_image_0000002193850624.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=559DF5793FF69049E18CD30BCB2CFC7B9148F12F7F1551F22D9D4ABC2578F735 "点击放大")

### pixelMap类型数据交互

本章以图片处理应用为例，介绍如何进行pixelMap类型数据交互。

除本文介绍的方法外，也可通过readPixelsToBuffer将其转换为Uint8Array类型，进行处理。此方案可以参考[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)，本文不作介绍。

说明

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加image的libpixelmap\_ndk.z.so

```
1. # entry/src/main/cpp/CMakeLists.txt
2. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libpixelmap_ndk.z.so)
```

[CMakeLists.txt](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/CMakeLists.txt#L20-L21)

**实现原理**

PixelMap是一种用于显示图像的数据结构。在C++侧接收该类型参数的时候，可以直接调用libpixelmap.so库中的函数直接通过ArkTS侧的pixelmap对象构造出Native侧的pixelmap类型对象（NativePixelMap），进而对其进行数据处理。

由于pixelMap类似一个C++语言中的指针，通过上述操作之后更改了其指向的内容，因此在ArkTS侧通过设定延迟可以直接触发ArkTS侧的图像自渲染，从而实现ArkTS页面刷新，直接显示修改后的图像。

**开发步骤**

1. 函数声明与调用，与[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)类同，此处不再赘述。
2. 在ArkTS侧，需要先完成图片的加载和pixelMap化。

   ```
   1. // entry/src/main/ets/pages/PixelMapPage.ets
   2. async loadPixelMap() {
   3. let resourceManager = this.getUIContext().getHostContext()!.resourceManager;
   4. try {
   5. let imageArray = await resourceManager.getMediaContent($r('app.media.SampleImage').id);
   6. let imageResource = image.createImageSource(imageArray.buffer);
   7. let opts: image.DecodingOptions = { editable: true, desiredPixelFormat: image.PixelMapFormat.BGRA_8888 };
   8. imageResource.createPixelMap(opts).then((pixelMap) => {
   9. this.pixelMap = pixelMap;
   10. this.loadComplete = true;
   11. })
   12. } catch (error) {
   13. let err = error as BusinessError;
   14. hilog.error(0x0000, 'testTag', `getMediaContent fail. code = ${err.code}, message = ${err.message}`);
   15. }
   16. }

   18. aboutToAppear(): void {
   19. this.loadPixelMap();
   20. }
   ```

   [PixelMapPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/PixelMapPage.ets#L37-L57)

   createPixelMap()：负责将从imageResource加载的图片解码为pixelMap格式。
3. 在C++工程中，定义数据传递函数。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. static napi_value PixelMapPassing(napi_env env, napi_callback_info info) {
   3. size_t argc = 1;
   4. napi_value ts_pixel_map;
   5. // Gets detailed information about the function call, such as input parameters.
   6. napi_get_cb_info(env, info, &argc, &ts_pixel_map, nullptr, nullptr);

   8. // Initialize the NativePixelMap object.
   9. // NativePixelMap and ArkTSPixelMap share memory space.
   10. // That is, modifications to NativePixelMap also affect ArkTSPixelMap.
   11. NativePixelMap *native_pixel_map = OH_PixelMap_InitNativePixelMap(env, ts_pixel_map);

   13. float opacity = 0.5;
   14. OH_PixelMap_SetOpacity(native_pixel_map, opacity);

   16. return nullptr;
   17. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L205-L221)

   napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

   OH\_PixelMap\_InitNativePixelMap()：负责初始化NativePixelMap对象。

   OH\_PixelMap\_SetOpacity()：负责修改NativePixelMap中的不透明度。

   其他诸如旋转、缩放等操作可以参考[位图操作（使用Image处理PixelMap数据）](../harmonyos-guides/image-pixelmap-operation-native.md)。

   说明

   输入的TSPixelMap与生成的NativePixelMap共享内存空间，因此直接调用相关方法修改NativePixelMap对象，即可同步影响TSPixelMap对象。所以此处无需回传数据。
4. 在Init()函数中的设置流程与[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)相同，不再赘述。
5. 在ArkTS中令Image组件重新渲染。

   ```
   1. // entry/src/main/ets/pages/PixelMapPage.ets
   2. if (this.loadComplete) {
   3. Image(this.pixelMap)
   4. .height(400)
   5. } else {
   6. Image($r('app.media.loading'))
   7. .height(400)
   8. }
   ```

   [PixelMapPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/PixelMapPage.ets#L63-L70)

   如上所示，通过更改this.loadComplete()即可完成Image的重新渲染。

   ```
   1. // entry/src/main/ets/pages/PixelMapPage.ets
   2. if (this.pixelMap) {
   3. this.loadComplete = false;
   4. ParamPassing.pixelMapPassing(this.pixelMap);
   5. // Only modifying PixelMap cannot cause the system to re render,
   6. // so this method is required to manually refresh the image component.
   7. setTimeout(() => this.loadComplete = true, 500);
   8. }
   ```

   [PixelMapPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/PixelMapPage.ets#L76-L83)

   这是因为pixelMap类似一个C语言指针，只更改其指向的内容，其本身值未变，不会引发自动重渲染。此处设定的延迟也是为了确保重渲染可以触发。

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/pnvU6F68SsyHUyA-R8xDmA/zh-cn_image_0000002194010228.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=5F612AAA03BD02A5C19142E8B849ECB0EA85D740FD78F5E34FD93BAEF9584FF9 "点击放大")

### class类型数据，ArkTS传递至C++

本章以简单的计算器为例，介绍如何进行class类型数据交互。由于两侧传递方式差异较大，因此分为两章讲解。

本章讲解ArkTS传递至C++。

**实现原理**

ArkTS语言中，class（类）是用于定义对象的模板，并拥有特有的属性和方法。在C++侧接收该类型时与object类型基本一致，一般会通过Node-API提供的函数（如napi\_get\_named\_property()）来获取class对象的某个属性，从而操作其属性值。

**开发步骤**

1. 在index.d.ts中声明需要传递的class。

   ```
   1. // entry/src/main/cpp/types/libentry/Index.d.ts
   2. export interface SampleClassTs2Napi {
   3. result: string;

   5. add(a: number, b: number): string;
   6. }
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/types/libentry/Index.d.ts#L30-L35)

   声明传递用的函数。

   ```
   1. // entry/src/main/cpp/types/libentry/Index.d.ts
   2. export const classPassingTs2Napi: (input: SampleClassTs2Napi) => string;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/types/libentry/Index.d.ts#L52-L53)

   ArkTS文件中也需要对此进行引用，并实现上文声明的class。

   ```
   1. // entry/src/main/ets/pages/ClassPage.ets
   2. import ParamPassing from 'libentry.so';
   3. import { OutputArea } from '../model/IOModel';

   5. const HINT_STRING: string = 'Calculation completed:\n';

   7. class SampleClassTs2Napi implements ParamPassing.SampleClassTs2Napi {
   8. public result: string = '';

   10. add(a: number, b: number) {
   11. this.result = `${a} + ${b} = ${a + b}`;
   12. return HINT_STRING;
   13. }
   14. }
   ```

   [ClassPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/ClassPage.ets#L17-L30)
2. 在C++工程中，定义数据传递函数。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. napi_value ClassPassingTs2Napi(napi_env env, napi_callback_info info) {
   3. size_t argc = 1;
   4. napi_value args;
   5. // Gets detailed information about the function call, such as input parameters.
   6. napi_get_cb_info(env, info, &argc, &args, nullptr, nullptr);

   8. // Retrieve the method named "add" from the parameter object and store it in the "add" variable.
   9. napi_value add;
   10. napi_get_named_property(env, args, "add", &add);

   12. // Create parameter array
   13. napi_value arr[2];
   14. napi_create_int32(env, 114, &arr[0]);
   15. napi_create_int32(env, 514, &arr[1]);
   16. // Call the "add" method of the parameter object, pass this array as a parameter,
   17. // and store the result in the funcResult variable.
   18. napi_value func_result;
   19. napi_call_function(env, args, add, 2, arr, &func_result);

   21. // Retrieve the property values named "result" from the parameter object
   22. // using the napi_get_named_property function, and store them in the param_result variables.
   23. napi_value param_result;
   24. napi_get_named_property(env, args, "result", &param_result);

   26. string resultStr = Value2String(env, func_result) + Value2String(env, param_result);
   27. return String2value(env, resultStr);
   28. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L225-L252)

   classPassingTs2Napi()：负责将class从ArkTS传递至Napi，之后返回一个string作为结果。

   napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

   napi\_get\_named\_property()：第一次调用，负责将方法名为"add"的方法存入变量add中。

   napi\_create\_int32()：负责将入参解析为int32，并存入数组arr中。

   napi\_call\_function()：负责在C++工程中调用从ArkTS传入的class的方法，需要使用上两步获得的入参数组arr和方法add。

   napi\_get\_named\_property()：第二次调用，负责将名为"result"的属性存入param\_result中。

   value2String、string2value()：负责napi\_value与string类型之间的相互转换，实现方法详见[hashMap类型数据交互](bpta-complex-type-pass.md#section81062596218)。
3. 需在DevEco Studio[预生成](bpta-complex-type-pass.md#fig08576372193)的Init()函数中设置写好的数据传递函数。与[arrayBuffer类型数据交互](bpta-complex-type-pass.md#section9552193517193)类同，此处不再赘述。

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/eJf8fOnXQqGa3Oqmoi2smw/zh-cn_image_0000002193850628.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=0B8FE77B8AFA68CC579C91AE528ED4CBCAC77DED091CBAE295E5D22341EA8C0C "点击放大")

### class类型数据，C++传递至ArkTS

本章仍以简单的计算器为例，介绍class类型数据如何从C++传递至ArkTS。

**实现原理**

从C++侧传递class类型到ArkTS侧时，需要在C++侧对C++类方法进行Napi适配，然后在init函数中通过napi\_define\_class建立ArkTS类方法与C++侧方法的映射关系，然后将对应的class对象挂载到export上导出。注意：需要在index.d.ts文件中声明需要传递的class。

**开发步骤**

1. 需要在index.d.ts中声明需要传递的class。

   ```
   1. // entry/src/main/cpp/types/libentry/Index.d.ts
   2. export class SampleClassNapi2Ts {
   3. private _hintStr: string;

   5. constructor(hintStr: string);

   7. times(a: number, b: number): string;
   8. public get hintStr();
   9. public set hintStr(value:string);
   10. }
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/types/libentry/Index.d.ts#L39-L48)

   说明

   此处需要使用get和set关键字定义访问器，不能直接引用、修改属性。
2. 在ArkTS侧调用该class及其属性、方法。

   ```
   1. // entry/src/main/ets/pages/ClassPage.ets
   2. let napiClass: ParamPassing.SampleClassNapi2Ts = new ParamPassing.SampleClassNapi2Ts(HINT_STRING);
   3. napiClass.hintStr += 'modify by ArkTS: \n';
   4. this.printStr = napiClass.hintStr + napiClass.times(6, 9);
   ```

   [ClassPage.ets](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/ets/pages/ClassPage.ets#L63-L66)

   在调用时，用法与其他寻常的ArkTS的class一样。无需特别注意。
3. 在C++工程中，定义对应的class。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. class SampleClassNapi2Ts {
   3. public:
   4. std::string hint_str;
   5. SampleClassNapi2Ts(string str) { this->hint_str = str; };
   6. std::string times(int a, int b) {
   7. std::ostringstream ost;
   8. ost << a << " × " << b << " = " << a * b;
   9. return ost.str();
   10. };
   11. };
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L256-L266)

   此处使用ostringstream输出流，以便完成字符串的构造。因此需要提前导入stream。

   同时，还需依次完成供ArkTS调用的访问器、构造函数和方法。

   1. getHintStr()，用于获取hintStr属性。

      ```
      1. // entry\src\main\cpp\napi_init.cpp
      2. static napi_value GetHintStr(napi_env env, napi_callback_info info) {
      3. napi_value ts_class_obj;
      4. // Gets detailed information about the function call, such as input parameters.
      5. napi_get_cb_info(env, info, nullptr, nullptr, &ts_class_obj, nullptr);

      7. SampleClassNapi2Ts *c_class_obj;
      8. // Retrieve and manipulate the C++object previously bound to jsThis using napi_unwrap
      9. napi_unwrap(env, ts_class_obj, reinterpret_cast<void **>(&c_class_obj));
      10. if (c_class_obj) {
      11. return String2value(env, c_class_obj->hint_str);
      12. } else {
      13. return nullptr;
      14. }
      15. }
      ```

      [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L298-L312)

   napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

   napi\_unwrap()：负责解析ArkTS class中包装的C++ class，并使用指针c\_class\_obj进行储存。

   string2value()：负责将obj->hintStr转换为napi\_value，作为输出。此函数的实现方法详见[hashMap类型数据交互](bpta-complex-type-pass.md#section81062596218)。

   ArkTS侧调用hintStr的值的时候，需要调用此函数，从而获得C++侧的hintStr的值。

   说明

   初始化阶段的访问器，napi\_unwrap后获得的c\_class\_obj可能为空指针，所以必须验空。下同。

   2. setHintStr()，用于设置hintStr属性。原理与getHintStr相通。

      ```
      1. // entry\src\main\cpp\napi_init.cpp
      2. static napi_value SetHintStr(napi_env env, napi_callback_info info) {
      3. // Obtain parameters transmitted from the TS layer
      4. size_t argc = 1;
      5. napi_value value;
      6. napi_value ts_class_obj;
      7. // Gets detailed information about the function call, such as input parameters.
      8. napi_get_cb_info(env, info, &argc, &value, &ts_class_obj, nullptr);

      10. SampleClassNapi2Ts *c_class_obj;
      11. // Retrieve and manipulate the C++object previously bound to jsThis using napi_unwrap
      12. napi_unwrap(env, ts_class_obj, reinterpret_cast<void **>(&c_class_obj));

      14. if (c_class_obj) {
      15. c_class_obj->hint_str = Value2String(env, value);
      16. }

      18. return nullptr;
      19. }
      ```

      [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L316-L334)
   3. 实现times方法，为加区分，此处命名为TSTimes。

      napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

      napi\_unwrap()：负责将传入的ArkTS class解包，获取与其绑定的C++ class，并使用指针c\_class\_obj进行储存。

      napi\_get\_value\_int32()：负责将入参解析为int32并存入value0/value1中。

      string2Value()：负责将string转换为napi\_value数据。此函数的实现方法详见[hashMap类型数据交互](bpta-complex-type-pass.md#section81062596218)。

      ```
      1. // entry\src\main\cpp\napi_init.cpp
      2. static napi_value TSTimes(napi_env env, napi_callback_info info) {
      3. size_t argc = 2;
      4. napi_value args[2] = {nullptr};
      5. napi_value ts_class_obj = nullptr;
      6. // Gets detailed information about the function call, such as input parameters.
      7. napi_get_cb_info(env, info, &argc, args, &ts_class_obj, nullptr);
      8. SampleClassNapi2Ts *c_class_obj = nullptr;
      9. // Convert ArkTS object to C++ object
      10. napi_unwrap(env, ts_class_obj, (void **)&c_class_obj);
      11. // Get parameters passed by ArkTS
      12. int value0;
      13. napi_get_value_int32(env, args[0], &value0);
      14. int value1;
      15. napi_get_value_int32(env, args[1], &value1);
      16. string c_result = c_class_obj->times(value0, value1);
      17. return String2value(env, c_result);
      18. }
      ```

      [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L338-L355)
   4. TsConstructor()，用于构造ArkTS class。

      napi\_get\_cb\_info()：负责从ArkTS侧获取输入参数。

      value2String()：负责将入参转换为string。此函数的实现方法详见[hashMap类型数据交互](bpta-complex-type-pass.md#section81062596218)。

      napi\_set\_named\_property()：负责对指定的object加入一个新属性，并指定属性名。ArkTS侧调用的时候，将使用此处指定的名称。

      napi\_wrap()：负责将C++ class包装为ArkTS class。

      ```
      1. // entry\src\main\cpp\napi_init.cpp
      2. static napi_value TsConstructor(napi_env env, napi_callback_info info) {
      3. // Create Napi object
      4. napi_value ts_class_obj;
      5. size_t argc = 1;
      6. napi_value args[1] = {nullptr};
      7. // Gets detailed information about the function call, such as input parameters.
      8. napi_get_cb_info(env, info, &argc, args, &ts_class_obj, nullptr);
      9. string hint_str = Value2String(env, args[0]);
      10. // Create C++ object
      11. SampleClassNapi2Ts *c_class_obj = new SampleClassNapi2Ts(hint_str);
      12. // Set the JS object hintStr attribute
      13. napi_set_named_property(env, ts_class_obj, "hintStr", args[0]);
      14. // Binding JS objects with C++objects
      15. napi_wrap(
      16. env, ts_class_obj, c_class_obj,
      17. // Define callback function for recycling JS objects, used to destroy C++objects and prevent memory leaks
      18. [](napi_env env, void *finalize_data, void *finalize_hint) {
      19. SampleClassNapi2Ts *c_class_obj = (SampleClassNapi2Ts *)finalize_data;
      20. delete c_class_obj;
      21. c_class_obj = nullptr;
      22. },
      23. nullptr, nullptr);
      24. return ts_class_obj;
      25. }
      ```

      [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L270-L294)
4. 在Init()函数中设置class。

   ```
   1. // entry\src\main\cpp\napi_init.cpp
   2. EXTERN_C_START
   3. static napi_value Init(napi_env env, napi_value exports) {
   4. // ...
   5. napi_property_descriptor class_prop[] = {
   6. {"hintStr", 0, 0, getHintStr, setHintStr, 0, napi_default, 0},
   7. {"times", nullptr, TSTimes, nullptr, nullptr, nullptr, napi_default, nullptr}};
   8. napi_value sample_class = nullptr;
   9. const char *class_name = "SampleClassNapi2Ts";
   10. // Establish the association between ArkTS constructor and C++ methods
   11. napi_define_class(env, class_name, sizeof(class_name), TsConstructor, nullptr,
   12. sizeof(class_prop) / sizeof(class_prop[0]), class_prop, &sample_class);
   13. napi_set_named_property(env, exports, class_name, sample_class);

   15. return exports;
   16. }
   17. EXTERN_C_END
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/ComplexTypePass/blob/master/entry/src/main/cpp/napi_init.cpp#L359-L391)

   需要先在DevEco Studio[预生成](bpta-complex-type-pass.md#fig08576372193)的Init()函数中，定义一个classProp，并写入class对应的访问器与方法

   并调用napi\_define\_class()和napi\_set\_named\_property()完成ArkTS class 与C++ class的关联与设置。从而令ArkTS可以调用C++中的class。

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/bR6oh4-3S9K1-OfTdYP40Q/zh-cn_image_0000002229450497.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=C44801FB5D91324DB70F22073E3CB3E0D5184CE7AAD3D82861602BDDD021353B "点击放大")

## 示例代码

* [实现复杂参数的跨语言交互功能](https://gitcode.com/harmonyos_samples/ComplexTypePass)
