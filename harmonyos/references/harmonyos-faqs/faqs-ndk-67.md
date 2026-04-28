---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-67
title: 如何实现ArkTS与C/C++的HashMap转换
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何实现ArkTS与C/C++的HashMap转换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2a039988e1663e7dd6ead6694ea9e85f7d88510deeafc4c3539f0d06b2809dee
---

**问题详情：**

如何实现将ArkTS的HashMap转换至Native侧。

**解决措施：**

* 方案一：传递数组。

  将HashMap的key、value作为数组取出，将两个数组传递至Native侧并组装成Map。

  ArkTS侧传递数组。

  ```
  1. let hashMap: HashMap<string, number> = new HashMap();
  2. hashMap.set("Abc", 123);
  3. hashMap.set("Bcd", 234);
  4. hashMap.set("Cde", 345);

  6. let keysArray: Array<string> = Array.from(hashMap.keys());
  7. let valuesArray: Array<number> = Array.from(hashMap.values());
  8. testNapi.tsPutMap(keysArray, valuesArray, hashMap.length);
  ```

  [HashMap.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/HashMap.ets#L50-L57)

  在Native侧组装Map。

  ```
  1. // Convert value to string and return
  2. std::string HashMap::value2String(napi_env env, napi_value value) {
  3. size_t stringSize = 0;
  4. napi_get_value_string_utf8(env, value, nullptr, 0, &stringSize); // 获取字符串长度
  5. std::string valueString;
  6. valueString.resize(stringSize + 1);
  7. napi_get_value_string_utf8(env, value, &valueString[0], stringSize + 1, &stringSize); // 根据长度转换成字符串
  8. return valueString;
  9. }
  10. napi_value HashMap::TsPutMap(napi_env env, napi_callback_info info) {
  11. std::map<std::string, int> myMap;
  12. size_t argc = 3;
  13. napi_value args[3] = {nullptr};
  14. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  15. napi_value mapKey = args[0]; // key
  16. napi_value mapVal = args[1]; // value
  17. napi_value mapNum = args[2]; // length

  20. uint32_t mapCNum = 0;
  21. napi_get_value_uint32(env, mapNum, &mapCNum);
  22. for (uint32_t i = 0; i < mapCNum; i++) {
  23. napi_value keyNIndex, valNIndex;
  24. napi_get_element(env, mapKey, i, &keyNIndex);
  25. napi_get_element(env, mapVal, i, &valNIndex);
  26. std::string keyIndex = value2String(env, keyNIndex);
  27. int valIndex = 0;
  28. napi_get_value_int32(env, valNIndex, &valIndex);
  29. myMap[keyIndex] = valIndex;
  30. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "Pure", "%{public}s %{public}d", keyIndex.c_str(), myMap[keyIndex]);
  31. }
  32. return nullptr;
  33. }
  ```

  [HashMap.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/HashMap/HashMap.cpp#L25-L57)
* 方案二：传递JSON。

  将HashMap转换为Json数据传至Native侧，在Native侧反序列化用Map承接。

  ArkTS侧转JSON。

  1. JSON.stringify不支持对HashMap操作，需要先将其转成Record

     ```
     1. map2rec(map: HashMap<string, ESObject>): Record<string, ESObject> {
     2. // Map to Record
     3. let Rec: Record<string, ESObject> = {}
     4. map.forEach((value: ESObject, key: string) => {
     5. if (value instanceof HashMap) {
     6. //Value may be HashMap
     7. let vRec: Record<string, ESObject> = this.map2rec(value)
     8. value = vRec
     9. }
     10. Rec[key] = value
     11. })
     12. return Rec
     13. }
     ```

     [HashMap.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/HashMap.ets#L27-L39)
  2. 然后使用JSON.stringify序列化

     ```
     1. let myRec: Record<string, ESObject> = this.map2rec(hashMap);
     2. let str: string = JSON.stringify(myRec);
     3. testNapi.mapJson(str);
     ```

     [HashMap.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/HashMap.ets#L61-L63)

  Native侧反序列化。

  C++没有直接反序列化的接口，需要使用三方库，本demo采用lycium交叉编译工具编译json三方库。

  ```
  1. napi_value HashMap::MapJson(napi_env env, napi_callback_info info) {

  3. size_t argc = 1;
  4. napi_value args[1] = {nullptr};
  5. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

  7. std::string jsonStr = value2String(env, args[0]);

  9. std::map<std::string, int> myMap = nlohmann::json::parse(jsonStr.c_str());

  11. OH_LOG_Print(LOG_APP, LOG_INFO, 0x0000, "Pure", "%{public}d %{public}d %{public}d", myMap["Abc"], myMap["Bcd"],
  12. myMap["Cde"]);

  14. return nullptr;
  15. }
  ```

  [HashMap.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/HashMap/HashMap.cpp#L61-L75)
