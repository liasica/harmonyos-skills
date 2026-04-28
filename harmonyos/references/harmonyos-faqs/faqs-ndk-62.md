---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-62
title: Native侧如何对ArkTS传递的Object类型的数据、属性进行修改
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何对ArkTS传递的Object类型的数据、属性进行修改
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4b3b4810f8960eed2736148aa6cdae3350529efb2ba0824dcf76e0247ad04415
---

1. ArkTS侧调用Native侧方法modifyObject，并传递参数。

   ```
   1. import testNapi from 'libentry.so';

   4. interface Obj1 {
   5. obj: Obj2,
   6. hello: String,
   7. arr: number[],
   8. typedArray: Uint8Array
   9. }

   12. interface Obj2 {
   13. str: string
   14. }

   17. @Entry
   18. @Component
   19. struct Index {
   20. @State message: string = 'Hello World';

   23. build() {
   24. Row() {
   25. Column() {
   26. Text(this.message)
   27. .fontSize(50)
   28. .fontWeight(FontWeight.Bold)
   29. .onClick(() => {
   30. const typedArr = new Uint8Array(3);
   31. typedArr[0] = 1;
   32. typedArr[1] = 2;
   33. typedArr[2] = 3;
   34. const obj: Obj1 = {
   35. obj: { str: 'obj in obj' },
   36. hello: 'world',
   37. arr: [94, 32, 43],
   38. typedArray: typedArr
   39. }
   40. console.info(`Test NAPI modifyObject result is ${JSON.stringify(testNapi.modifyObject(obj))}`)
   41. })
   42. }
   43. .width('100%')
   44. }
   45. .height('100%')
   46. }
   47. }
   ```

   [RevArkTSObj.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/RevArkTSObj.ets#L19-L65)

   index.d.ts声明导出接口。

   ```
   1. export const modifyObject: (a: object) => object;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/types/libentry/Index.d.ts#L47-L47)
2. Native侧解析参数并修改数据、属性

   ```
   1. #include "RevArkTSObj.h"
   2. napi_value RevArkTSObj::ModifyObject(napi_env env, napi_callback_info info) {
   3. size_t argc = 1;
   4. napi_value args[1] = {nullptr};
   5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

   8. napi_value obj = args[0];

   11. napi_value obj1;
   12. napi_value hello1;
   13. napi_value arr1;
   14. napi_value typedArray1;

   17. napi_get_named_property(env, obj, "obj", &obj1);
   18. char *buf = "this is modified";
   19. napi_value str1;
   20. napi_create_string_utf8(env, buf, NAPI_AUTO_LENGTH, &str1);
   21. napi_set_named_property(env, obj1, "str", str1);
   22. napi_set_named_property(env, obj, "obj", obj1);

   25. napi_create_string_utf8(env, "world0", NAPI_AUTO_LENGTH, &hello1);
   26. napi_set_named_property(env, obj, "hello", hello1);

   29. napi_get_named_property(env, obj, "arr", &arr1);
   30. uint32_t arrLen;
   31. napi_get_array_length(env, arr1, &arrLen);
   32. for (int i = 0; i < arrLen; i++) {
   33. napi_value tmp;
   34. napi_create_uint32(env, i, &tmp);
   35. napi_set_element(env, arr1, i, tmp);
   36. }
   37. napi_delete_element(env, arr1, 2, nullptr);

   42. napi_get_named_property(env, obj, "typedArray", &typedArray1);
   43. bool is_typedArray;
   44. if (napi_ok != napi_is_typedarray(env, typedArray1, &is_typedArray)) {
   45. return nullptr;
   46. }
   47. napi_typedarray_type type;
   48. napi_value input_buffer;
   49. size_t length;
   50. size_t byte_offset;
   51. napi_get_typedarray_info(env, typedArray1, &type, &length, nullptr, &input_buffer, &byte_offset);
   52. // Retrieve the basic data buffer data of input_fuffer and the length byte_length of the basic data buffer.
   53. void *data;
   54. size_t byte_length;
   55. napi_get_arraybuffer_info(env, input_buffer, &data, &byte_length);
   56. // Create a new ArrayBuffer with a pointer pointing to the underlying data buffer of the ArrayBuffer, denoted as' output _ptr '
   57. napi_value output_buffer;
   58. void *output_prt = nullptr;
   59. napi_create_arraybuffer(env, byte_length, &output_prt, &output_buffer);
   60. // Create typedarray using output buffer
   61. napi_value output_array;
   62. napi_create_typedarray(env, type, length, output_buffer, byte_offset, &output_array);
   63. // Data is composed of consecutive memory locations, where reinterpret_cast<uint8_t *>(data) represents the memory address of its first element.
   64. // Data is the old arraybuffer data pointer
   65. uint8_t *input_bytes = reinterpret_cast<uint8_t *>(data) + byte_offset;
   66. // Assign the 'outputting _ptr' pointer to 'outputting: bytes'
   67. // Output_ptr is a new array buffer data pointer
   68. uint8_t *output_bytes = reinterpret_cast<uint8_t *>(output_prt);
   69. for (int i = 0; i < length; i++) {
   70. // Multiply each element of the old arraybuffer data by 2 and assign it to the new arraybuffer data
   71. output_bytes[i] = input_bytes[i] * 2;
   72. }
   73. // Assign the new typedArray to obj ['typedArray ']
   74. napi_set_named_property(env, obj, "typedArray", output_array);
   75. return obj;
   76. }
   ```

   [RevArkTSObj.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/RevArkTSObj/RevArkTSObj.cpp#L19-L94)
3. 输出结果：

   Test NAPI modifyObject result is {"obj":{"str":"this is modified"},"hello":"world0","arr":[0,1,null],"typedArray":{"0":2,"1":4,"2":6}}
