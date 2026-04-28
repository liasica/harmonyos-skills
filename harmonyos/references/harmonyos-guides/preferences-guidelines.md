---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preferences-guidelines
title: 通过用户首选项实现数据持久化 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过用户首选项实现数据持久化 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8af2c8061d9c8376d552b23cdbe15d7d5274e067a3f65dd873461823ca435149
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

```
1. libohpreferences.so
```

## 引用头文件

```
1. #include <database/preferences/oh_preferences.h>
2. #include <database/preferences/oh_preferences_err_code.h>
3. #include <database/preferences/oh_preferences_option.h>
4. #include <database/preferences/oh_preferences_value.h>
```

## 开发步骤

下列实例展示如何通过Preferences实现对键值数据的修改与持久化。

1. 创建Preferences配置选项（PreferencesOption）对象并设置配置选项成员（名称、应用组ID、包名、存储模式）。使用完毕后，调用OH\_PreferencesOption\_Destroy销毁配置选项实例。
2. 调用OH\_Preferences\_Open打开一个Preferences实例，该实例使用完后需要调用OH\_Preferences\_Close关闭。

   ```
   1. // 1. 创建Preferences配置选项。
   2. OH_PreferencesOption *option = OH_PreferencesOption_Create();
   3. if (option == nullptr) {
   4. // 错误处理
   5. }
   6. // 设置Preferences配置选项的文件名称。
   7. int ret = OH_PreferencesOption_SetFileName(option, "testdb");
   8. if (ret != PREFERENCES_OK) {
   9. (void)OH_PreferencesOption_Destroy(option);
   10. // 错误处理
   11. }
   12. // 设置Preferences配置选项的应用组ID。
   13. ret = OH_PreferencesOption_SetDataGroupId(option, "");
   14. if (ret != PREFERENCES_OK) {
   15. (void)OH_PreferencesOption_Destroy(option);
   16. // 错误处理
   17. }
   18. // 设置Preferences配置选项的包名称。
   19. ret = OH_PreferencesOption_SetBundleName(option, "com.example");
   20. if (ret != PREFERENCES_OK) {
   21. (void)OH_PreferencesOption_Destroy(option);
   22. // 错误处理
   23. }
   24. // 设置Preferences配置选项的存储模式，需要注意的是，设置之前需要调用OH_Preferences_IsStorageTypeSupported接口判断当前平台是否支持需要选择的模式。
   25. bool isGskvSupported = false;
   26. ret = OH_Preferences_IsStorageTypeSupported(Preferences_StorageType::PREFERENCES_STORAGE_GSKV, &isGskvSupported);
   27. if (ret != PREFERENCES_OK) {
   28. (void)OH_PreferencesOption_Destroy(option);
   29. // 错误处理
   30. }
   31. if (isGskvSupported) {
   32. ret = OH_PreferencesOption_SetStorageType(option, Preferences_StorageType::PREFERENCES_STORAGE_GSKV);
   33. if (ret != PREFERENCES_OK) {
   34. (void)OH_PreferencesOption_Destroy(option);
   35. // 错误处理
   36. }
   37. } else {
   38. ret = OH_PreferencesOption_SetStorageType(option, Preferences_StorageType::PREFERENCES_STORAGE_XML);
   39. if (ret != PREFERENCES_OK) {
   40. (void)OH_PreferencesOption_Destroy(option);
   41. // 错误处理
   42. }
   43. }
   44. // 2. 打开一个Preferences实例。
   45. int errCode = PREFERENCES_OK;
   46. OH_Preferences *preference = OH_Preferences_Open(option, &errCode);
   47. // option使用完毕后可直接释放，释放后需要将指针置空。
   48. (void)OH_PreferencesOption_Destroy(option);
   49. option = nullptr;
   50. if (preference == nullptr || errCode != PREFERENCES_OK) {
   51. // 错误处理
   52. }
   53. // option使用完毕后删除配置选项
   54. errCode = OH_Preferences_DeletePreferences(option);
   55. if (errCode != PREFERENCES_OK) {
   56. // 错误处理
   57. }
   ```
3. 订阅回调函数为DataChangeObserverCallback。

   ```
   1. // 数据变更回调函数
   2. void DataChangeObserverCallback(void *context, const OH_PreferencesPair *pairs, uint32_t count)
   3. {
   4. for (uint32_t i = 0; i < count; i++) {
   5. // 获取索引i对应的PreferencesValue
   6. const OH_PreferencesValue *pValue = OH_PreferencesPair_GetPreferencesValue(pairs, i);
   7. // 获取PreferencesValue的数据类型
   8. Preference_ValueType type = OH_PreferencesValue_GetValueType(pValue);
   9. int ret = PREFERENCES_OK;
   10. if (type == PREFERENCE_TYPE_INT) {
   11. int intValue = 0;
   12. ret = OH_PreferencesValue_GetInt(pValue, &intValue);
   13. if (ret == PREFERENCES_OK) {
   14. // 业务逻辑
   15. }
   16. } else if (type == PREFERENCE_TYPE_BOOL) {
   17. bool boolValue = true;
   18. ret = OH_PreferencesValue_GetBool(pValue, &boolValue);
   19. if (ret == PREFERENCES_OK) {
   20. // 业务逻辑
   21. }
   22. } else if (type == PREFERENCE_TYPE_STRING) {
   23. char *stringValue = nullptr;
   24. uint32_t valueLen = 0;
   25. ret = OH_PreferencesValue_GetString(pValue, &stringValue, &valueLen);
   26. if (ret == PREFERENCES_OK) {
   27. // 业务逻辑
   28. OH_Preferences_FreeString(stringValue);
   29. }
   30. } else {
   31. // 无效类型
   32. }
   33. }
   34. }
   ```

   调用OH\_Preferences\_RegisterDataObserver注册3个Key的数据变更订阅。

   ```
   1. // 3. 对key_int、key_bool和key_string注册数据变更订阅。
   2. const char *keys[] = {"key_int", "key_bool", "key_string"};
   3. int ret = OH_Preferences_RegisterDataObserver(preference, nullptr, DataChangeObserverCallback, keys, 3);
   4. if (ret != PREFERENCES_OK) {
   5. (void)OH_Preferences_Close(preference);
   6. // 错误处理
   7. }
   8. // 兼容多种类型的注册数据变更订阅。
   9. int contextData = 42;
   10. ret = OH_Preferences_RegisterMultiProcessDataObserver(preference, &contextData, DataChangeObserverCallback);
   11. if (ret != PREFERENCES_OK) {
   12. // 错误处理
   13. }
   14. // 取消兼容多种类型的注册数据变更订阅。
   15. ret = OH_Preferences_UnregisterMultiProcessDataObserver(preference, &contextData, DataChangeObserverCallback);
   16. if (ret != PREFERENCES_OK) {
   17. // 错误处理
   18. }
   ```
4. 设置Preferences实例中的键值数据。

   ```
   1. // 4. 设置Preferences实例中的KV数据。
   2. ret = OH_Preferences_SetInt(preference, keys[0], 0);
   3. if (ret != PREFERENCES_OK) {
   4. (void)OH_Preferences_Close(preference);
   5. // 错误处理
   6. }
   7. ret = OH_Preferences_SetBool(preference, keys[1], true);
   8. if (ret != PREFERENCES_OK) {
   9. (void)OH_Preferences_Close(preference);
   10. // 错误处理
   11. }
   12. int32_t stringIndex = 2;
   13. ret = OH_Preferences_SetString(preference, keys[stringIndex], "string value");
   14. if (ret != PREFERENCES_OK) {
   15. (void)OH_Preferences_Close(preference);
   16. // 错误处理
   17. }
   18. ret = OH_Preferences_Flush(preference);
   19. if (ret != PREFERENCES_OK) {
   20. (void)OH_Preferences_Close(preference);
   21. // 错误处理
   22. }
   23. OH_PreferencesValue* setIntValue = OH_PreferencesValue_Create();
   24. if (setIntValue  == nullptr) {
   25. // 错误处理
   26. }
   27. const int value = 456;
   28. ret = OH_PreferencesValue_SetInt(setIntValue, value);
   29. if (ret != PREFERENCES_OK) {
   30. (void)OH_PreferencesValue_Destroy(setIntValue);
   31. // 错误处理
   32. }
   33. ret = OH_Preferences_SetValue(preference, "int_key", setIntValue);
   34. if (ret != PREFERENCES_OK) {
   35. (void)OH_Preferences_Close(preference);
   36. // 错误处理
   37. }
   ```
5. 获取Preferences实例中的键值数据。

   ```
   1. // 5. 获取Preferences实例中的KV数据。
   2. int intValue = 0;
   3. int ret = PREFERENCES_OK;
   4. const char *keys[] = {"key_int", "key_bool", "key_string"};
   5. ret = OH_Preferences_GetInt(preference, keys[0], &intValue);
   6. if (ret == PREFERENCES_OK) {
   7. // 业务逻辑
   8. }

   10. bool boolValue = false;
   11. ret = OH_Preferences_GetBool(preference, keys[1], &boolValue);
   12. if (ret == PREFERENCES_OK) {
   13. // 业务逻辑
   14. }

   16. char *stringValue = nullptr;
   17. uint32_t valueLen = 0;
   18. int32_t stringIndex = 2;
   19. ret = OH_Preferences_GetString(preference, keys[stringIndex], &stringValue, &valueLen);
   20. if (ret == PREFERENCES_OK) {
   21. // 业务逻辑
   22. // 使用完OH_Preferences_GetString接口后，需要对字符串进行释放。
   23. OH_Preferences_FreeString(stringValue);
   24. stringValue = nullptr;
   25. }

   27. OH_PreferencesValue* getIntValue = OH_PreferencesValue_Create();
   28. if (getIntValue  == nullptr) {
   29. // 错误处理
   30. }
   31. ret = OH_Preferences_GetValue(preference, "int_key", &getIntValue);
   32. if (ret == PREFERENCES_OK) {
   33. // 业务逻辑
   34. }

   36. OH_PreferencesPair* pairs = nullptr;
   37. uint32_t count = 0;
   38. ret = OH_Preferences_GetAll(preference, &pairs, &count);
   39. if (ret == PREFERENCES_OK) {
   40. // 业务逻辑
   41. if (pairs != nullptr) {
   42. // 销毁例对象中所有的KV数据。
   43. OH_PreferencesPair_Destroy(pairs, count);
   44. }
   45. }

   47. // 查询Preferences实例中的Key是否有数据
   48. bool result = OH_Preferences_HasKey(preference, "int_key");
   49. if (result == true) {
   50. // 有数据 业务逻辑
   51. }

   53. // 清理缓存数据
   54. ret = OH_Preferences_ClearCache(preference);
   ```
6. 调用OH\_Preferences\_Close关闭Preferences实例，关闭后需要将实例指针置空。

   ```
   1. // 6. 使用完Preferences实例后需要关闭实例，关闭后需要将指针置空。
   2. (void)OH_Preferences_Close(preference);
   3. preference = nullptr;
   ```
7. 设置和获取OH\_PreferencesValue数据。

   ```
   1. const int arg5 = 5;
   2. const int arg4 = 4;
   3. const int arg3 = 3;
   4. int ret = PREFERENCES_OK;
   5. OH_PreferencesValue* setValue = OH_PreferencesValue_Create();
   6. bool boolArray[] = {true, false, true, false};
   7. ret = OH_PreferencesValue_SetBoolArray(setValue, boolArray, arg4);
   8. if (ret != PREFERENCES_OK) {
   9. // 错误处理
   10. }
   11. uint32_t count = 0;
   12. bool* outBoolArray = nullptr;
   13. ret = OH_PreferencesValue_GetBoolArray(setValue, &outBoolArray, &count);
   14. if (ret != PREFERENCES_OK) {
   15. // 错误处理
   16. }

   18. const char* strArray[] = {"hello", "world", "test"};
   19. ret = OH_PreferencesValue_SetStringArray(setValue, strArray, arg3);
   20. if (ret != PREFERENCES_OK) {
   21. // 错误处理
   22. }
   23. char** outStrArray = nullptr;
   24. ret = OH_PreferencesValue_GetStringArray(setValue, &outStrArray, &count);
   25. if (ret != PREFERENCES_OK) {
   26. // 错误处理
   27. }

   29. int64_t int64Array[] = {1234567890LL, 9876543210LL, -1234567890LL};
   30. ret = OH_PreferencesValue_SetInt64Array(setValue, int64Array, arg3);
   31. if (ret != PREFERENCES_OK) {
   32. // 错误处理
   33. }
   34. int64_t* outArrayInt64 = nullptr;
   35. ret = OH_PreferencesValue_GetInt64Array(setValue, &outArrayInt64, &count);
   36. if (ret != PREFERENCES_OK) {
   37. // 错误处理
   38. }

   40. double doubleArray[] = {1.1, 2.2, 3.3, 4.4};
   41. ret = OH_PreferencesValue_SetDoubleArray(setValue, doubleArray, arg4);
   42. if (ret != PREFERENCES_OK) {
   43. // 错误处理
   44. }
   45. double* outDoubleArray = nullptr;
   46. ret = OH_PreferencesValue_GetDoubleArray(setValue, &outDoubleArray, &count);
   47. if (ret != PREFERENCES_OK) {
   48. // 错误处理
   49. }

   51. uint8_t blobData[] = {0x01, 0x02, 0x03, 0x04, 0x05};
   52. ret = OH_PreferencesValue_SetBlob(setValue, blobData, arg5);
   53. if (ret != PREFERENCES_OK) {
   54. // 错误处理
   55. }
   56. uint8_t* outBlob = nullptr;
   57. ret = OH_PreferencesValue_GetBlob(setValue, &outBlob, &count);
   58. if (ret != PREFERENCES_OK) {
   59. // 错误处理
   60. }
   ```
