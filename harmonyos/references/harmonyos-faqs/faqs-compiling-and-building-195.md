---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
title: 编译报错：pnpm安装失败等问题汇总
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错：pnpm安装失败等问题汇总
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:50+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:cc5f2f9eff196897ad904394dde6790ce098839eabfbc1ab9275b6bcc0814a1a
---

**问题现象**

执行sync或构建命令时，编译报错：“ERROR: 003080xx Operation Error”。

常见错误码为：00308019-00308024

**背景知识**

00308019-00308024错误码为开发者在hvigor-config.json5中新增js包依赖，执行sync或编译时在“Build Init”阶段编译的报错。报错原因为pnpm/npm工具安装包时失败。

**场景一：ERROR: 00308019 Operation Error**

**报错现象：**

```
1. > hvigor ERROR: 00308019 Operation Error
2. Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
3. ERR_PNPM_FETCH_404  GET https://xxx/npm-central-repo/testX:  - 404
4. This error happened while installing a direct dependency of C:\Users\xxx\.hvigor\project_caches\4cfxxx4f5\workspace
5. testX is not in the npm registry, or you have no permission to fetch it.
6. No authorization header was set for the request.
7. * Try the following:
8. > Check whether the failed package exists in the npm repository.
9. > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```

**常见原因：**

hvigor-config.json5中dependencies字段中配置了形如 testX: '3.3.10'的包，hvigor初始化时调用pnpm工具安装tesXt@3.3.10包，但是在pnpm仓库中找不到匹配的包名testX。常见为包的名称写错，或者pnpm仓库地址配置错误，或者没有权限访问此包。

**解决措施：**

1、在电脑console控制台上，运行`pnpm view xxx versions`命令查看xxx包在仓库里是否存在。

2、请联系xxx包的提供方，明确xxx包的仓库地址，及访问权限，然后修改本地pnpm的配置。

**场景二：ERROR: 00308020 Operation Error**

**报错现象：**

```
1. > hvigor ERROR: 00308020 Operation Error
2. Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
3. ERR_PNPM_NO_MATCHING_VERSION  No matching version found for test@3.3.10 while fetching it from https://xxx/npm-central-repo/
4. This error happened while installing a direct dependency of C:\Users\xxx\.hvigor\project_caches\4cf***4f5\workspace
5. The latest release of test is "3.3.0". Published at 2023/12/8
6. If you need the full list of all 3 published versions run "$ pnpm view test versions".
7. * Try the following:
8. > Check whether the version of the failed package exists in the npm repository.
9. > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```

**常见原因：**

hvigor-config.json5中dependencies字段中配置了 test: '3.3.10'的包，hvigor初始化时调用pnpm工具安装test@3.3.10包，但是在pnpm仓库中找不到匹配的版本。常见为包的版本写错，或者pnpm仓库地址配置错误。

**解决措施：**

1、在电脑console控制台上，运行`pnpm view xxx versions`命令查看xxx包在仓库里的可用版本，使用可用的版本。

2、如果要使用的版本在pnpm仓库里不存在，请联系xxx包的提供方，明确xxx包的仓库地址，然后修改本地pnpm的仓库地址。

**场景三：ERROR: 00308021 Operation Error**

**报错现象：**

```
1. > hvigor ERROR: 00308021 Operation Error
2. Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
3. WARN  GET https://xxx/test error (ETIMEDOUT). Will retry in 10 seconds. 2 retries left.
4. WARN  GET https://xxx/test error (ETIMEDOUT). Will retry in 1 minute. 1 retries left.
5. ERR_PNPM_META_FETCH_FAIL  GET https://xxx/test: request to https://xxx/test failed, reason: connect ETIMEDOUT xxx.xxx.xxx.xxx:443.
6. This error happened while installing a direct dependency of xxx.
7. * Try the following:
8. > Ensure that the npm repository address is accessible.
9. > Contact the repository provider or replace the npm repository address.
10. > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```

**常见原因：**

hvigor-config.json5中dependencies字段中配置了test包，hvigor初始化时调用pnpm工具安装test包，但是链接超时在远程仓库中找不到test包的元数据。常见为网络问题，或者pnpm仓库地址配置错误。

**解决措施：**

1、在电脑console控制台上，运行install命令查看是否可以正常安装。

2、请确保仓库地址可以访问，查看npm配置的仓库地址是否正确、是否有防火墙或代理限制等。

3、联系仓库提供方确认仓库地址是否可用，或更换新的npm仓库地址。

**场景四：ERROR: 00308022 Operation Error**

**报错现象：**

```
1. > hvigor ERROR: 00308022 Operation Error
2. Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
3. ERR_PNPM_NO_OFFLINE_META Failed to resolve test@1.2.3 in package mirror xxx.
4. This error happened while installing a direct dependency of xxx.
5. * Try the following:
6. > Check whether the offline package has been completely downloaded before the migration.
7. > Refer to 'Setting Up the Development Environment Offline': https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-no-network
8. > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```

**常见原因：**

hvigor-config.json5中dependencies字段中配置了test包，且使用离线安装模式，pnpm在离线模式下，无法从本地缓存中找到某个依赖包的元数据。常见为包的相关依赖没有打包完整，导致离线环境下无法找到。

**解决措施：**

1、请检查离线包在迁移前是否已下载完整。

2、参考[离线环境配置指导](../harmonyos-guides/ide-no-network.md)。

**场景五：ERROR: 00308023 Operation Error**

**报错现象：**

```
1. > hvigor ERROR: 00308023 Operation Error
2. Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
3. npm ERR! code CERT_HAS_EXPIRED
4. npm ERR! errno CERT_HAS_EXPIRED
5. npm ERR! request to https://xxx failed, reason: certificate has expired
6. npm ERR! A complete log of this run can be found in: xxx
7. * Try the following:
8. > Contact the npm repository provider to ensure that the certificate of the repository server is valid, or replace the repository address with a new one.
9. > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```

**常见原因：**

hvigor-config.json5中dependencies字段中配置了test包，但是hvigor初始化构建时，安装依赖时链接npm远程仓库失败。常见为npm仓库服务器证书过期。

**解决措施：**

请联系仓库提供方确保仓库服务器的证书有效，或更换新的npm仓库地址。

**场景六：ERROR: 00308024 Operation Error**

**报错现象：**

```
1. > hvigor ERROR: 00308024 Operation Error
2. Error Message: C:\Users\xxx\.hvigor\wrapper\tools\node_modules\.bin\pnpm.cmd install execute failed. More details:
3. npm ERR! code ETIMEDOUT
4. npm ERR! errno ETIMEDOUT
5. npm ERR! request to https://xxx failed, reason: connect ETIMEDOUT xxx.xxx.xxx.xxx:443
6. This error happened while installing a direct dependency of xxx.
7. * Try the following:
8. > Ensure that the npm repository address is accessible.
9. > Contact the repository provider or replace the npm repository address.
10. > More info: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-195
```

**常见原因：**

hvigor-config.json5中dependencies字段中配置了test包，但是hvigor初始化构建时，链接npm仓库超时。常见为代理、防火墙限制或npm仓库地址失效等导致无法访问。

**解决措施：**

1、请确保仓库地址可以访问，查看npm配置的仓库地址是否正确、是否有防火墙或代理限制等。

2、联系仓库提供方确认仓库地址是否可用，或更换新的npm仓库地址。
