---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-31
title: 如何在Native侧集成三方库Curl，并进行HTTP数据请求
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧集成三方库Curl，并进行HTTP数据请求
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:08a96c7b1c09cd4e6157aa2b8ea12b5de4db763e6f4ac9d790cabca01e38b70b
---

可以将Curl移植到HarmonyOS，并在Native侧开发时直接使用Curl的C++库实现。具体的移植方法请参考相关链接。

具体使用步骤如下：

1. 将移植后的Curl的so库放入Native工程的entry/libs/arm64-v8a/目录，将包含头文件的include目录放入entry/src/main/cpp目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/BLDwORnwS2C62cnmqQECYA/zh-cn_image_0000002194158760.png?HW-CC-KV=V1&HW-CC-Date=20260428T002434Z&HW-CC-Expire=86400&HW-CC-Sign=4836098D000098D5B49F54C3998AC14E4B724A527705219CB3B84308248F8919 "点击放大")
2. 在CMakeLists.txt文件中链接Curl对应的so库。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/GB2qfpt7SfOP4ZsU5FL-3A/zh-cn_image_0000002194158764.png?HW-CC-KV=V1&HW-CC-Date=20260428T002434Z&HW-CC-Expire=86400&HW-CC-Sign=479E3B3087D4ABF3E6F31D044780CA9AAC65C21616C1BDC81798AFFEE52A1C33 "点击放大")
3. 在Native侧的.cpp文件中引入头文件curl.h，使用Curl的相关能力。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/q4CXsIJQTqy_AXr70-8E7g/zh-cn_image_0000002229758629.png?HW-CC-KV=V1&HW-CC-Date=20260428T002434Z&HW-CC-Expire=86400&HW-CC-Sign=BCDF09D09A8897559AFA131C9AC4BBEEBD603C8FE06B06C52BA5139153DFBBC3 "点击放大")

   具体可参考以下代码：

   ```
   1. #include "curl/curl.h"

   3. // ...

   5. // Get request and post request data response functions
   6. size_t ReqReply(void *ptr, size_t size, size_t nmemb, void *userdata) {
   7. string *str = reinterpret_cast<string *>(userdata);
   8. (*str).append((char *)ptr, size * nmemb);
   9. return size * nmemb;
   10. }

   12. // http GET Request configuration
   13. CURLcode CurlGetReq(const std::string &url, std::string &response) {
   14. // Curl initialization
   15. CURL *curl = curl_easy_init();
   16. // Curl return value
   17. CURLcode res;
   18. if (curl) {
   19. // Set the request header for Curl
   20. struct curl_slist *headers = NULL;
   21. headers = curl_slist_append(headers, "Content-Type:application/json");
   22. curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

   24. // Set the URL address for the request
   25. curl_easy_setopt(curl, CURLOPT_URL, url.c_str());

   27. // Receive response header data, 0 represents not receiving, 1 represents receiving
   28. curl_easy_setopt(curl, CURLOPT_HEADER, 1);

   30. // Set data receiving function
   31. curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, ReqReply);
   32. curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&response);

   34. // Set to not use any signal/alarm handlers
   35. curl_easy_setopt(curl, CURLOPT_NOSIGNAL, 1);

   37. // Set timeout period
   38. curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 10);
   39. curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10);

   41. // Open request
   42. res = curl_easy_perform(curl);
   43. }
   44. // Release curl
   45. curl_easy_cleanup(curl);
   46. return res;
   47. }

   50. static napi_value NatReq(napi_env env, napi_callback_info info) {
   51. string getUrlStr = "http://app.huawei.com";
   52. string getResponseStr;
   53. auto res = CurlGetReq(getUrlStr, getResponseStr);
   54. if (res == CURLE_OK) {
   55. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "pure", "response: \n%{public}s", getResponseStr.c_str());
   56. }

   58. // ...
   59. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Curl_Request/entry/src/main/cpp/hello.cpp#L21-L107)

结果展示

终端使用curl指令获取的网站信息一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/4B0LVU1LQvWmb2l4lqmxug/zh-cn_image_0000002229604137.png?HW-CC-KV=V1&HW-CC-Date=20260428T002434Z&HW-CC-Expire=86400&HW-CC-Sign=623D78B31F4383FEB8DA154BFDF679DCC2316EADFD19AD1F56E501B05BB09141 "点击放大")

**参考链接**

[使用命令行CMake构建NDK工程](../harmonyos-guides/build-with-ndk-cmake.md)

[使用lycium工具快速编译三方库](../best-practices/bpta-lycium-adapts-to-harmonyos.md)
