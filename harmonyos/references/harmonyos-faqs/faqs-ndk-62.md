---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-62
title: Native侧如何对ArkTS传递的Object类型的数据、属性进行修改
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何对ArkTS传递的Object类型的数据、属性进行修改
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:14574681b6693ba6c8bd9d709381d6b7e931bb09b324418b449f7d9a8018051f
---

1. ArkTS侧调用Native侧方法modifyObject，并传递参数。

   ```ts
   import testNapi from 'libentry.so';

   interface Obj1 {
     obj: Obj2,
     hello: String,
     arr: number[],
     typedArray: Uint8Array
   }

   interface Obj2 {
     str: string
   }

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               const typedArr = new Uint8Array(3);
               typedArr[0] = 1;
               typedArr[1] = 2;
               typedArr[2] = 3;
               const obj: Obj1 = {
                 obj: { str: 'obj in obj' },
                 hello: 'world',
                 arr: [94, 32, 43],
                 typedArray: typedArr
               }
               console.info(`Test NAPI modifyObject result is ${JSON.stringify(testNapi.modifyObject(obj))}`)
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

   index.d.ts声明导出接口。

   ```ts
   export const modifyObject: (a: object) => object;
   ```
2. Native侧解析参数并修改数据、属性

   ```cpp
   #include "RevArkTSObj.h"
   napi_value RevArkTSObj::ModifyObject(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value args[1] = {nullptr};
       napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

       napi_value obj = args[0];

       napi_value obj1;
       napi_value hello1;
       napi_value arr1;
       napi_value typedArray1;

       napi_get_named_property(env, obj, "obj", &obj1);
       char *buf = "this is modified";
       napi_value str1;
       napi_create_string_utf8(env, buf, NAPI_AUTO_LENGTH, &str1);
       napi_set_named_property(env, obj1, "str", str1);
       napi_set_named_property(env, obj, "obj", obj1);

       napi_create_string_utf8(env, "world0", NAPI_AUTO_LENGTH, &hello1);
       napi_set_named_property(env, obj, "hello", hello1);

       napi_get_named_property(env, obj, "arr", &arr1);
       uint32_t arrLen;
       napi_get_array_length(env, arr1, &arrLen);
       for (int i = 0; i < arrLen; i++) {
           napi_value tmp;
           napi_create_uint32(env, i, &tmp);
           napi_set_element(env, arr1, i, tmp);
       }
       napi_delete_element(env, arr1, 2, nullptr);

       napi_get_named_property(env, obj, "typedArray", &typedArray1);
       bool is_typedArray;
       if (napi_ok != napi_is_typedarray(env, typedArray1, &is_typedArray)) {
           return nullptr;
       }
       napi_typedarray_type type;
       napi_value input_buffer;
       size_t length;
       size_t byte_offset;
       napi_get_typedarray_info(env, typedArray1, &type, &length, nullptr, &input_buffer, &byte_offset);
       // Retrieve the basic data buffer data of input_fuffer and the length byte_length of the basic data buffer.
       void *data;
       size_t byte_length;
       napi_get_arraybuffer_info(env, input_buffer, &data, &byte_length);
       // Create a new ArrayBuffer with a pointer pointing to the underlying data buffer of the ArrayBuffer, denoted as' output _ptr '
       napi_value output_buffer;
       void *output_prt = nullptr;
       napi_create_arraybuffer(env, byte_length, &output_prt, &output_buffer);
       // Create typedarray using output buffer
       napi_value output_array;
       napi_create_typedarray(env, type, length, output_buffer, byte_offset, &output_array);
       // Data is composed of consecutive memory locations, where reinterpret_cast<uint8_t *>(data) represents the memory address of its first element.
       // Data is the old arraybuffer data pointer
       uint8_t *input_bytes = reinterpret_cast<uint8_t *>(data) + byte_offset;
       // Assign the 'outputting _ptr' pointer to 'outputting: bytes'
       // Output_ptr is a new array buffer data pointer
       uint8_t *output_bytes = reinterpret_cast<uint8_t *>(output_prt);
       for (int i = 0; i < length; i++) {
           // Multiply each element of the old arraybuffer data by 2 and assign it to the new arraybuffer data
           output_bytes[i] = input_bytes[i] * 2;
       }
       // Assign the new typedArray to obj ['typedArray ']
       napi_set_named_property(env, obj, "typedArray", output_array);
       return obj;
   }
   ```
3. 输出结果：

   Test NAPI modifyObject result is {"obj":{"str":"this is modified"},"hello":"world0","arr":[0,1,null],"typedArray":{"0":2,"1":4,"2":6}}
