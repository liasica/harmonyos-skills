---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-21
title: 使用NAPI扩展TS接口时，常用属性和实现接口的基本用法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 使用NAPI扩展TS接口时，常用属性和实现接口的基本用法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3606a4b27042cf4920c69d6cd66a6730111796a8fc86426af9cb16e99a09c361
---

1. env是使用NAPI的模块化编程，注册模块后，通过回调函数调用。

   ```ts
   static napi_value CallNapi(napi_env env, napi_callback_info info) { 
       size_t argc = 1; 
       napi_value object = nullptr; 
       napi_status status; 
       status = napi_get_cb_info(env, info, &argc, &object, nullptr, nullptr); 
       return object; 
   } 
   NAPI_MODULE_INIT() { 
       napi_property_descriptor desc[] = { 
           { "callNapi", nullptr, CallNapi, nullptr, nullptr, nullptr, napi_default, nullptr } 
       }; 
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc); 
       return exports; 
   }
   ```
2. 实现回调：

   ```screen
   #include "napi/native_api.h" 
   #include <assert.h> 
   static napi_value NativeCall(napi_env env, napi_callback_info info) { 
       size_t argc = 1; 
       napi_value args[1] = { nullptr }; 
       napi_status status; 
       status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr); 
       assert(status == napi_ok); 
       napi_valuetype valuetype; 
       napi_typeof(env, args[0], &valuetype); 
       if (valuetype != napi_valuetype::napi_function) { 
           napi_throw_type_error(env, nullptr, "napi_function is expected"); 
       } 
       napi_value cb = args[0]; 
       napi_value undefined; 
       status = napi_get_undefined(env, &undefined); 
       assert(status == napi_ok); 
       napi_value argv[2] = { nullptr }; 
       status = napi_create_int32(env, 1, &argv[0]); 
       assert(status == napi_ok); 
       status = napi_create_int32(env, 2, &argv[1]); 
       assert(status == napi_ok); 
       napi_value result; 
       status = napi_call_function(env, undefined, cb, 2, argv, &result); 
       assert(status == napi_ok); 
       return nullptr; 
   } 
   EXTERN_C_START 
   static napi_value Init(napi_env env, napi_value exports) { 
       napi_property_descriptor desc[] = { 
           { "nativeCall", nullptr, NativeCall, nullptr, nullptr, nullptr, napi_default, nullptr } 
       }; 
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc); 
       return exports; 
   } 
   EXTERN_C_END 
   static napi_module module = { 
       .nm_version = 1, 
       .nm_flags = 0, 
       .nm_filename = nullptr, 
       .nm_register_func = Init, 
       .nm_modname = "callback", 
       .nm_priv = nullptr, 
       .reserved = { 0 }, 
   }; 
   extern "C" __attribute__((constructor)) void RegisterCallbackModule(void) { 
       napi_module_register(&module); 
   }
   ```
3. Promise实现参考：

   ```cpp
   #include "napi/native_api.h" 
   // Empty value so that macros here are able to return NULL or void 
   #define NAPI_RETVAL_NOTHING  // Intentionally blank 
   #define GET_AND_THROW_LAST_ERROR(env)                                                                    
       do {                                                                                               
           const napi_extended_error_info* errorInfo = nullptr;                                             
           napi_get_last_error_info((env), &errorInfo);                                                     
           bool isPending = false;                                                                          
           napi_is_exception_pending((env), &isPending);                                                    
           if (!isPending && errorInfo != nullptr) {                                                        
               const char* errorMessage =                                                                   
                   errorInfo->error_message != nullptr ? errorInfo->error_message : "empty error message";  
               napi_throw_error((env), nullptr, errorMessage);                                              
           }                                                                                                
       } while (0) 
   #define NAPI_ASSERT_BASE(env, assertion, message, retVal)                                     
       do {                                                                                      
           if (!(assertion)) {                                                                   
               napi_throw_error((env), nullptr, "assertion ("#assertion") failed:" message);  
               return retVal;                                                                    
           }                                                                                     
       } while (0) 
   #define NAPI_ASSERT(env, assertion, message) NAPI_ASSERT_BASE(env, assertion, message, nullptr) 
   #define NAPI_ASSERT_RETURN_VOID(env, assertion, message)  
           NAPI_ASSERT_BASE(env, assertion, message, NAPI_RETVAL_NOTHING) 
   #define NAPI_CALL_BASE(env, theCall, retVal)  
       do {                                      
           if ((theCall) != napi_ok) {           
               GET_AND_THROW_LAST_ERROR((env));  
               return retVal;                    
           }                                     
       } while (0) 
   #define NAPI_CALL(env, theCall) NAPI_CALL_BASE(env, theCall, nullptr) 
   #define NAPI_CALL_RETURN_VOID(env, theCall) NAPI_CALL_BASE(env, theCall, NAPI_RETVAL_NOTHING) 
   struct AsyncData { 
       napi_deferred deferred; 
       napi_async_work work; 
       int32_t arg; 
       double retVal; 
   }; 
   double DoSomething(int32_t val) { 
       if (val != 0) { 
           return 1.0 / val;  
       } 
       return 0; 
   } 
   void ExecuteCallback(napi_env env, void* data) { 
       AsyncData* asyncData = reinterpret_cast<AsyncData*>(data); 
       asyncData->retVal = DoSomething(asyncData->arg); 
   } 
   void CompleteCallback(napi_env env, napi_status status, void* data) { 
       AsyncData* asyncData = reinterpret_cast<AsyncData*>(data); 
       napi_value retVal; 
       if (asyncData->retVal == 0) { 
           NAPI_CALL_RETURN_VOID(env, napi_create_string_utf8(env, "arg can't be zero", NAPI_AUTO_LENGTH, &retVal)); 
           NAPI_CALL_RETURN_VOID(env, napi_reject_deferred(env, asyncData->deferred, retVal)); 
       } else { 
           NAPI_CALL_RETURN_VOID(env, napi_create_double(env, asyncData->retVal, &retVal)); 
           NAPI_CALL_RETURN_VOID(env, napi_resolve_deferred(env, asyncData->deferred, retVal)); 
       } 
       NAPI_CALL_RETURN_VOID(env, napi_delete_async_work(env, asyncData->work)); 
       asyncData->work = nullptr; 
       asyncData->deferred = nullptr; 
       delete asyncData; 
   } 
   static napi_value NativeCall(napi_env env, napi_callback_info info) { 
       size_t argc = 1; 
       napi_value args[1] = { nullptr }; 
       NAPI_CALL(env, napi_get_cb_info(env, info, &argc, args, nullptr, nullptr)); 
       int32_t arg; 
       NAPI_CALL(env, napi_get_value_int32(env, args[0], &arg)); 
       // Create promise 
       napi_deferred deferred; 
       napi_value promise; 
       NAPI_CALL(env, napi_create_promise(env, &deferred, &promise)); 
       AsyncData* data = new AsyncData; 
       data->deferred = deferred; 
       data->arg = arg; 
       napi_async_work work; 
       napi_value workName; 
       napi_create_string_utf8(env, "promise", NAPI_AUTO_LENGTH, &workName); 
       NAPI_CALL(env, napi_create_async_work(env, nullptr, workName,ExecuteCallback, CompleteCallback, data, &work)); 
       data->work = work; 
       NAPI_CALL(env, napi_queue_async_work(env, work)); 
       return promise; 
   } 
   EXTERN_C_START 
   static napi_value Init(napi_env env, napi_value exports) { 
       napi_property_descriptor desc[] = { 
           { "nativeCall", nullptr, NativeCall, nullptr, nullptr, nullptr, napi_default, nullptr } 
       }; 
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc); 
       return exports; 
   } 
   EXTERN_C_END 
   static napi_module demoModule = { 
       .nm_version = 1, 
       .nm_flags = 0, 
       .nm_filename = nullptr, 
       .nm_register_func = Init, 
       .nm_modname = "promise", 
       .nm_priv = nullptr, 
       .reserved = { 0 }, 
   }; 
   extern "C" __attribute__((constructor)) void RegisterPromiseModule(void) { 
       napi_module_register(&demoModule); 
   }
   ```
4. 使用libuv：直接导入[libuv](../harmonyos-references/libuv.md)库。
