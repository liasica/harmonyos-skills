---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-sample
title: 实践说明
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 配置多目标产物 > 实践说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ad7c140ae6732b05622d50d8455700035301c935dae09c3c486c5cfc1eba8033
---

某对外发布应用共有两个版本：

1. Community社区版本，免费，向个人开发者用户提供该应用绝大部分基础功能，但是不提供部分定制化限定功能及技术支持。

2. Ultimate终极版本，收费，向个人、政企等开发者用户提供该应用全部基础功能，同时提供定制化限定功能及技术支持。

可以看出在Community版本与Ultimate版本之间，部分功能存在重合，同时也存在某些特定功能，所以期望通过一次开发以实现差异化，根据不同配置完成多种特定运行环境的开发、预览、打包、调试等功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/fEiyS0YBRymvVKDtEnqBjg/zh-cn_image_0000002530913126.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=D57DD54FDD484F7EE07C963048B8297667AD7D57CB673057BCCCA7C84316A292)

1. 两个不同版本的软件，可能存在差异：如不同的应用标题、应用图标、版本声明。我们可以在工程级build-profile.json5->app{}->products[]中，可以对两种不同的外发版本进行差异化定制，新增两个product：Community和Ultimate。根据已支持的字段进行定制修改。

```
1. {
2. "name": "Ultimate",
3. // ultimate版本签名
4. "signingConfig": "Ultimate",
5. // ultimate版本包名
6. "bundleName": "com.example.ultimate.app",
7. // ultimate版本应用图标
8. "icon": "$media:app_icon",
9. // ultimate版本应用标签
10. "label": "$string:app_name",
11. "versionCode": 10000,
12. "versionName": "1.0.0",
13. // ultimate版本指定资源目录
14. "resource": {
15. "directories": [
16. "./AppScope/ultimateRes"
17. ]
18. },
19. // ultimate版本指定输出产物名
20. "output": {
21. "artifactName": "ultimate_version"
22. },
23. "bundleType": "app",
24. "compatibleSdkVersion": "6.1.0(23)",
25. "runtimeOS": "HarmonyOS"
26. },
27. {
28. "name": "Community",
29. "signingConfig": "Community",
30. // community版本签名
31. "bundleName": "com.example.community.app",
32. // community版本包名
33. "icon": "$media:app_icon",
34. // community版本应用图标
35. "label": "$string:app_name",
36. // community版本应用标签
37. "versionCode": 10000,
38. "versionName": "1.0.0",
39. // community版本指定资源目录
40. "resource": {
41. "directories": [
42. "./AppScope/communityRes"
43. ]
44. },
45. // community版本指定输出产物名
46. "output": {
47. "artifactName": "community_version"
48. },
49. "bundleType": "app",
50. "compatibleSdkVersion": "6.1.0(23)",
51. "runtimeOS": "HarmonyOS",
52. }
```

2. 应用软件部分功能可能针对特定场景存在定制场景：如ultimate版本的功能A在phone设备类型上免费，在TV设备类型上需要收费；再如community版本的功能B在2in1设备类型上的启动页与在wearable设备类型上呈现效果存在差异。在模块级build-profile.json5->targets[]中新增2个 target：vip和free。

```
1. {
2. "name": "vip",
3. // 定制vip包输出产物名
4. "output": {
5. "artifactName": "vipVersion"
6. },
7. // 定制vip包源码指定页面
8. "source": {
9. "pages": [
10. "pages/vipIndex"
11. ]
12. },
13. // 指定vip包资源目录
14. "resource": {
15. "directories": [
16. "./src/main/ultimateRes"
17. ]
18. },
19. "config": {
20. // 指定vip包适用设备类型
21. "deviceType": [
22. "phone",
23. "tablet",
24. "2in1"
25. ]
26. }
27. },
28. {
29. "name": "free",
30. // 定制free包输出产物名
31. "output": {
32. "artifactName": "freeVersion"
33. },
34. // 定制free包源码指定页面
35. "source": {
36. "pages": [
37. "pages/freeIndex"
38. ]
39. },
40. // 指定free包资源目录
41. "resource": {
42. "directories": [
43. "./src/main/communityRes"
44. ]
45. },
46. "config": {
47. // 指定free包适用设备类型
48. "deviceType": [
49. "phone",
50. "tablet"
51. ]
52. }
53. }
```

3. 新增product、target后，需要在工程级build-profile.json5->modules[]->targets[]->applyToProducts中，指定关联关系。此处表示当前模块的target具体应用到工程product的配置。

```
1. "targets": [
2. {
3. "name": "default",
4. "applyToProducts": [
5. "default",
6. "Community",
7. "Ultimate"
8. ]
9. },
10. {
11. "name": "free",
12. "applyToProducts": [
13. "default",
14. "Community"
15. ]
16. },
17. {
18. "name": "vip",
19. "applyToProducts": [
20. "default",
21. "Ultimate"
22. ]
23. }
24. ]
```

由上配置：

* target：default被应用至product：default、Ultimate、Community中；
* target：vip被应用至product：default、Ultimate中；
* target：free被应用至product：default、Community中。

4. 在实际构建中，可通过可视化窗口灵活选择product-target的关联关系以构建出需要的APP/HAP包。

例：用户需要构建Ultimate版本的且具有vip特性的应用，可以选择product：Ultimate，target：vip，apply之后执行构建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/APkGa42HRfaiCXGgZxYf_Q/zh-cn_image_0000002561753063.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=504422978B6F719DCF9806CBD8A852DAF3F545EBA28C726141FB36C9169AFBF6)

查看构建产物

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/tbc589ZxTuyTNDK81S34Hw/zh-cn_image_0000002561753065.png?HW-CC-KV=V1&HW-CC-Date=20260427T235712Z&HW-CC-Expire=86400&HW-CC-Sign=0A24B040302117CEE164CEFB7EF4FEEA0F70FBB0DE2C9C9727FFA656049D2281)
