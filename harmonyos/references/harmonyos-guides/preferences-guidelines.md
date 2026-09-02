---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preferences-guidelines
title: 通过用户首选项实现数据持久化 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过用户首选项实现数据持久化 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ed2c6a45f19021c198ecc9c0021735622d750c3476bc9936b2eb9637e9b6a591
---

## 场景介绍

用户首选项（Preferences）模块主要提供轻量级Key-Value操作，支持本地存储少量数据，数据存储在文件和内存中，访问速度快。如果存在大量数据场景，请考虑使用键值型数据库或关系型数据库。

## 约束限制

* API version 18之前：ArkTS API仅支持[XML存储模式](data-persistence-by-preferences.md#xml存储)；C API仅支持[GSKV存储模式](data-persistence-by-preferences.md#gskv存储)；存储模式互不兼容，不支持ArkTS和C API操作同一个Preferences实例。
* API version 18及之后：ArkTS和C API均支持XML和GSKV双模式；ArkTS和C API使用相同的存储模式时，可以正常操作同一Preferences实例；禁止ArkTS和C API选择不同的存储模式，来操作同一个Preferences实例。
* Key的最大长度限制为1024个字节，Value的最大长度限制为16MB。

## 接口说明

详细的接口说明请参考[Preferences接口文档](../harmonyos-references/capi-preferences.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_Preferences \* OH\_Preferences\_Open (OH\_PreferencesOption \*option, int \*errCode) | 打开一个Preferences实例对象并创建指向它的指针。 当不再需要使用指针时，请使用OH\_Preferences\_Close关闭实例对象。 |
| int OH\_Preferences\_Close (OH\_Preferences \*preference) | 关闭一个Preferences实例对象。 |
| int OH\_Preferences\_GetInt (OH\_Preferences \*preference, const char \*key, int \*value) | 获取Preferences实例对象中Key对应的整型值。 |
| int OH\_Preferences\_GetBool (OH\_Preferences \*preference, const char \*key, bool \*value) | 获取Preferences实例对象中Key对应的布尔值。 |
| int OH\_Preferences\_GetString (OH\_Preferences \*preference, const char \*key, char \*\*value, uint32\_t \*valueLen) | 获取Preferences实例对象中Key对应的字符串。 |
| void OH\_Preferences\_FreeString (char \*string) | 释放从Preferences实例对象中获取的字符串。 |
| int OH\_Preferences\_SetInt (OH\_Preferences \*preference, const char \*key, int value) | 根据Key设置Preferences实例对象中的整型值。 |
| int OH\_Preferences\_SetBool (OH\_Preferences \*preference, const char \*key, bool value) | 根据Key设置Preferences实例对象中的布尔值。 |
| int OH\_Preferences\_SetString (OH\_Preferences \*preference, const char \*key, const char \*value) | 根据Key设置Preferences实例对象中的字符串。 |
| int OH\_Preferences\_Delete (OH\_Preferences \*preference, const char \*key) | 在Preferences实例对象中删除Key对应的KV数据。 |
| int OH\_Preferences\_RegisterDataObserver (OH\_Preferences \*preference, void \*context, OH\_PreferencesDataObserver observer, const char \*keys[], uint32\_t keyCount) | 对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH\_Preferences\_Close()后触发回调。 |
| int OH\_Preferences\_UnregisterDataObserver (OH\_Preferences \*preference, void \*context, OH\_PreferencesDataObserver observer, const char \*keys[], uint32\_t keyCount) | 取消注册选取Key的数据变更订阅。 |
| int OH\_Preferences\_IsStorageTypeSupported (Preferences\_StorageType type, bool \*isSupported) | 检查当前平台是否支持对应的存储模式。 |
| OH\_PreferencesOption \* OH\_PreferencesOption\_Create (void) | 创建一个Preferences配置选项的OH\_PreferencesOption实例对象以及指向它的指针。 当不再需要使用指针时，请使用OH\_PreferencesOption\_Destroy销毁实例对象，否则会导致内存泄漏。 |
| int OH\_PreferencesOption\_SetFileName (OH\_PreferencesOption \*option, const char \*fileName) | 设置Preferences配置选项OH\_PreferencesOption实例对象的文件名称。名称长度为0到255字节，其中不能包含'/'。 |
| int OH\_PreferencesOption\_SetBundleName (OH\_PreferencesOption \*option, const char \*bundleName) | 设置Preferences配置选项OH\_PreferencesOption实例对象的包名称。 |
| int OH\_PreferencesOption\_SetDataGroupId (OH\_PreferencesOption \*option, const char \*dataGroupId) | 设置Preferences配置选项OH\_PreferencesOption实例对象的应用组ID。 |
| int OH\_PreferencesOption\_SetStorageType (OH\_PreferencesOption \*option, Preferences\_StorageType type) | 设置Preferences配置选项 OH\_PreferencesOption实例对象的存储模式。 |
| int OH\_PreferencesOption\_Destroy (OH\_PreferencesOption \*option) | 销毁Preferences配置选项OH\_PreferencesOption实例。 |
| const char \* OH\_PreferencesPair\_GetKey (const OH\_PreferencesPair \*pairs, uint32\_t index) | 获取KV数据中索引对应数据的键。 |
| const OH\_PreferencesValue \* OH\_PreferencesPair\_GetPreferencesValue (const OH\_PreferencesPair \*pairs, uint32\_t index) | 获取KV数据数组中索引对应的值。 |
| Preference\_ValueType OH\_PreferencesValue\_GetValueType (const OH\_PreferencesValue \*object) | 获取PreferencesValue对象的数据类型。 |
| int OH\_PreferencesValue\_GetInt (const OH\_PreferencesValue \*object, int \*value) | 从PreferencesValue对象OH\_PreferencesValue中获取一个整型值。 |
| int OH\_PreferencesValue\_GetBool (const OH\_PreferencesValue \*object, bool \*value) | 从PreferencesValue对象OH\_PreferencesValue中获取一个布尔值。 |
| int OH\_PreferencesValue\_GetString (const OH\_PreferencesValue \*object, char \*\*value, uint32\_t \*valueLen) | 从PreferencesValue对象OH\_PreferencesValue中获取字符串。 |

## 添加动态链接库

CMakeLists.txt中添加以下lib。

```txt
libohpreferences.so
```

## 引用头文件

```
#include <database/preferences/oh_preferences.h>
#include <database/preferences/oh_preferences_err_code.h>
#include <database/preferences/oh_preferences_option.h>
#include <database/preferences/oh_preferences_value.h>
```

## 开发步骤

下列实例展示如何通过Preferences实现对键值数据的修改与持久化。

1. 创建Preferences配置选项（PreferencesOption）对象并设置配置选项成员（名称、应用组ID、包名、存储模式）。使用完毕后，调用OH\_PreferencesOption\_Destroy销毁配置选项实例。
2. 调用OH\_Preferences\_Open打开一个Preferences实例，该实例使用完后需要调用OH\_Preferences\_Close关闭。

   ```
   // 1. 创建Preferences配置选项。
   OH_PreferencesOption *option = OH_PreferencesOption_Create();
   if (option == nullptr) {
       // 错误处理
   }
   // 设置Preferences配置选项的文件名称。
   int ret = OH_PreferencesOption_SetFileName(option, "testdb");
   if (ret != PREFERENCES_OK) {
       (void)OH_PreferencesOption_Destroy(option);
       // 错误处理
   }
   // 设置Preferences配置选项的应用组ID。
   ret = OH_PreferencesOption_SetDataGroupId(option, "");
   if (ret != PREFERENCES_OK) {
       (void)OH_PreferencesOption_Destroy(option);
       // 错误处理
   }
   // 设置Preferences配置选项的包名称。
   ret = OH_PreferencesOption_SetBundleName(option, "com.example");
   if (ret != PREFERENCES_OK) {
       (void)OH_PreferencesOption_Destroy(option);
       // 错误处理
   }
   // 设置Preferences配置选项的存储模式，需要注意的是，设置之前需要调用OH_Preferences_IsStorageTypeSupported接口判断当前平台是否支持需要选择的模式。
   bool isGskvSupported = false;
   ret = OH_Preferences_IsStorageTypeSupported(Preferences_StorageType::PREFERENCES_STORAGE_GSKV, &isGskvSupported);
   if (ret != PREFERENCES_OK) {
       (void)OH_PreferencesOption_Destroy(option);
       // 错误处理
   }
   if (isGskvSupported) {
       ret = OH_PreferencesOption_SetStorageType(option, Preferences_StorageType::PREFERENCES_STORAGE_GSKV);
       if (ret != PREFERENCES_OK) {
           (void)OH_PreferencesOption_Destroy(option);
           // 错误处理
       }
   } else {
       ret = OH_PreferencesOption_SetStorageType(option, Preferences_StorageType::PREFERENCES_STORAGE_XML);
       if (ret != PREFERENCES_OK) {
           (void)OH_PreferencesOption_Destroy(option);
           // 错误处理
       }
   }
   // 2. 打开一个Preferences实例。
   int errCode = PREFERENCES_OK;
   OH_Preferences *preference = OH_Preferences_Open(option, &errCode);
   // option使用完毕后可直接释放，释放后需要将指针置空。
   (void)OH_PreferencesOption_Destroy(option);
   option = nullptr;
   if (preference == nullptr || errCode != PREFERENCES_OK) {
       // 错误处理
   }
   // option使用完毕后删除配置选项
   errCode = OH_Preferences_DeletePreferences(option);
   if (errCode != PREFERENCES_OK) {
       // 错误处理
   }
   ```
3. 订阅回调函数为DataChangeObserverCallback。

   ```
   // 数据变更回调函数
   void DataChangeObserverCallback(void *context, const OH_PreferencesPair *pairs, uint32_t count)
   {
       for (uint32_t i = 0; i < count; i++) {
           // 获取索引i对应的PreferencesValue
           const OH_PreferencesValue *pValue = OH_PreferencesPair_GetPreferencesValue(pairs, i);
           // 获取PreferencesValue的数据类型
           Preference_ValueType type = OH_PreferencesValue_GetValueType(pValue);
           int ret = PREFERENCES_OK;
           if (type == PREFERENCE_TYPE_INT) {
               int intValue = 0;
               ret = OH_PreferencesValue_GetInt(pValue, &intValue);
               if (ret == PREFERENCES_OK) {
                   // 业务逻辑
               }
           } else if (type == PREFERENCE_TYPE_BOOL) {
               bool boolValue = true;
               ret = OH_PreferencesValue_GetBool(pValue, &boolValue);
               if (ret == PREFERENCES_OK) {
                   // 业务逻辑
               }
           } else if (type == PREFERENCE_TYPE_STRING) {
               char *stringValue = nullptr;
               uint32_t valueLen = 0;
               ret = OH_PreferencesValue_GetString(pValue, &stringValue, &valueLen);
               if (ret == PREFERENCES_OK) {
                   // 业务逻辑
                   OH_Preferences_FreeString(stringValue);
               }
           } else {
               // 无效类型
           }
       }
   }
   ```

   调用OH\_Preferences\_RegisterDataObserver注册3个Key的数据变更订阅。

   ```
   // 3. 对key_int、key_bool和key_string注册数据变更订阅。
   const char *keys[] = {"key_int", "key_bool", "key_string"};
   int ret = OH_Preferences_RegisterDataObserver(preference, nullptr, DataChangeObserverCallback, keys, 3);
   if (ret != PREFERENCES_OK) {
       (void)OH_Preferences_Close(preference);
       // 错误处理
   }
   // 兼容多种类型的注册数据变更订阅。
   int contextData = 42;
   ret = OH_Preferences_RegisterMultiProcessDataObserver(preference, &contextData, DataChangeObserverCallback);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   // 取消兼容多种类型的注册数据变更订阅。
   ret = OH_Preferences_UnregisterMultiProcessDataObserver(preference, &contextData, DataChangeObserverCallback);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   ```
4. 设置Preferences实例中的键值数据。

   ```
   // 4. 设置Preferences实例中的KV数据。
   ret = OH_Preferences_SetInt(preference, keys[0], 0);
   if (ret != PREFERENCES_OK) {
       (void)OH_Preferences_Close(preference);
       // 错误处理
   }
   ret = OH_Preferences_SetBool(preference, keys[1], true);
   if (ret != PREFERENCES_OK) {
       (void)OH_Preferences_Close(preference);
       // 错误处理
   }
   int32_t stringIndex = 2;
   ret = OH_Preferences_SetString(preference, keys[stringIndex], "string value");
   if (ret != PREFERENCES_OK) {
       (void)OH_Preferences_Close(preference);
       // 错误处理
   }
   ret = OH_Preferences_Flush(preference);
   if (ret != PREFERENCES_OK) {
       (void)OH_Preferences_Close(preference);
       // 错误处理
   }
   OH_PreferencesValue* setIntValue = OH_PreferencesValue_Create();
   if (setIntValue  == nullptr) {
       // 错误处理
   }
   const int value = 456;
   ret = OH_PreferencesValue_SetInt(setIntValue, value);
   if (ret != PREFERENCES_OK) {
       (void)OH_PreferencesValue_Destroy(setIntValue);
       // 错误处理
   }
   ret = OH_Preferences_SetValue(preference, "int_key", setIntValue);
   if (ret != PREFERENCES_OK) {
       (void)OH_Preferences_Close(preference);
       // 错误处理
   }
   ```
5. 获取Preferences实例中的键值数据。

   ```
   // 5. 获取Preferences实例中的KV数据。
   int intValue = 0;
   int ret = PREFERENCES_OK;
   const char *keys[] = {"key_int", "key_bool", "key_string"};
   ret = OH_Preferences_GetInt(preference, keys[0], &intValue);
   if (ret == PREFERENCES_OK) {
       // 业务逻辑
   }
       
   bool boolValue = false;
   ret = OH_Preferences_GetBool(preference, keys[1], &boolValue);
   if (ret == PREFERENCES_OK) {
       // 业务逻辑
   }
       
   char *stringValue = nullptr;
   uint32_t valueLen = 0;
   int32_t stringIndex = 2;
   ret = OH_Preferences_GetString(preference, keys[stringIndex], &stringValue, &valueLen);
   if (ret == PREFERENCES_OK) {
       // 业务逻辑
       // 使用完OH_Preferences_GetString接口后，需要对字符串进行释放。
       OH_Preferences_FreeString(stringValue);
       stringValue = nullptr;
   }

   OH_PreferencesValue* getIntValue = OH_PreferencesValue_Create();
   if (getIntValue  == nullptr) {
       // 错误处理
   }
   ret = OH_Preferences_GetValue(preference, "int_key", &getIntValue);
   if (ret == PREFERENCES_OK) {
       // 业务逻辑
   }

   OH_PreferencesPair* pairs = nullptr;
   uint32_t count = 0;
   ret = OH_Preferences_GetAll(preference, &pairs, &count);
   if (ret == PREFERENCES_OK) {
       // 业务逻辑
       if (pairs != nullptr) {
           // 销毁例对象中所有的KV数据。
           OH_PreferencesPair_Destroy(pairs, count);
       }
   }

   // 查询Preferences实例中的Key是否有数据
   bool result = OH_Preferences_HasKey(preference, "int_key");
   if (result == true) {
       // 有数据 业务逻辑
   }

   // 清理缓存数据
   ret = OH_Preferences_ClearCache(preference);
   ```
6. 调用OH\_Preferences\_Close关闭Preferences实例，关闭后需要将实例指针置空。

   ```
   // 6. 使用完Preferences实例后需要关闭实例，关闭后需要将指针置空。
   (void)OH_Preferences_Close(preference);
   preference = nullptr;
   ```
7. 设置和获取OH\_PreferencesValue数据。

   ```
   const int arg5 = 5;
   const int arg4 = 4;
   const int arg3 = 3;
   int ret = PREFERENCES_OK;
   OH_PreferencesValue* setValue = OH_PreferencesValue_Create();
   bool boolArray[] = {true, false, true, false};
   ret = OH_PreferencesValue_SetBoolArray(setValue, boolArray, arg4);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   uint32_t count = 0;
   bool* outBoolArray = nullptr;
   ret = OH_PreferencesValue_GetBoolArray(setValue, &outBoolArray, &count);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }

   const char* strArray[] = {"hello", "world", "test"};
   ret = OH_PreferencesValue_SetStringArray(setValue, strArray, arg3);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   char** outStrArray = nullptr;
   ret = OH_PreferencesValue_GetStringArray(setValue, &outStrArray, &count);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }

   int64_t int64Array[] = {1234567890LL, 9876543210LL, -1234567890LL};
   ret = OH_PreferencesValue_SetInt64Array(setValue, int64Array, arg3);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   int64_t* outArrayInt64 = nullptr;
   ret = OH_PreferencesValue_GetInt64Array(setValue, &outArrayInt64, &count);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }

   double doubleArray[] = {1.1, 2.2, 3.3, 4.4};
   ret = OH_PreferencesValue_SetDoubleArray(setValue, doubleArray, arg4);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   double* outDoubleArray = nullptr;
   ret = OH_PreferencesValue_GetDoubleArray(setValue, &outDoubleArray, &count);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }

   uint8_t blobData[] = {0x01, 0x02, 0x03, 0x04, 0x05};
   ret = OH_PreferencesValue_SetBlob(setValue, blobData, arg5);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   uint8_t* outBlob = nullptr;
   ret = OH_PreferencesValue_GetBlob(setValue, &outBlob, &count);
   if (ret != PREFERENCES_OK) {
       // 错误处理
   }
   ```
