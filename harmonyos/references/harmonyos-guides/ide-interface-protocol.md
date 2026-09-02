---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-interface-protocol
title: ohpm仓库接口协议
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 附录 > ohpm仓库接口协议
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a0ddce7877699403d6d5bfe2696dc1e44c95baa94074f6e7e1aa72d66364a008
---

## 概述

ohpm客户端与ohpm-repo私仓通过REST API交互，目前一共如下几种API：

1. **Fetch Metadata**：用于获取三方库的元数据。三方库的下载地址也是元数据的一部分，具体的下载操作可以由ohpm-repo内部实现，也可以使用[存储插件](ide-ohpm-repo-storageplugin.md)，代理给其它文件服务实现。无论采用哪种实现方式，在ohpm客户端向返回的下载地址发起请求时，如果ohpm-repo配置不支持[匿名访问](ide-ohpm-system-settings.md#section71112584105)，或请求的仓库设置了授权可读，或请求的三方库的包权限设置了授权可读，ohpm客户端必须配置只读/读写认证，在下载请求的Http Header中，通过Authorization字段携带相应的Access Token，ohpm客户端才能正确下载；如需拉取精简元数据，则需要在下载请求的Http Header中，通过x-ohpm-metadata-type字段，携带value值为"install+v1"，即可返回精简元数据。
2. **Login（可选）**: 用于客户端登录。在使用公私钥认证时，ohpm客户端通过Login API从ohpm-repo获取一个Token，然后在调用publish，unpublish和dist-tags等API时，会在Http Header的Authorization字段携带相应的Token；如果选用Access Token的认证方式，则不需要实现该API。
3. **Login\_pss（可选）**：接口作用同Login接口。与Login接口差异：签名算法升级，由传统的RSA-SHA256 变更为 RSA-PSS（Probabilistic Signature Scheme）填充模式。
4. **Publish**：用于发布一个三方库到ohpm-repo私仓，需要先进行读写权限认证。
5. **Unpublish**：用于从ohpm-repo私仓下架（删除）一个三方库（下架一个包的某个版本或所有版本），需要先进行读写权限认证。
6. **Ping**：用于检测与ohpm-repo仓库的网络连通性，不需要任何认证。
7. **DistTags**：用于管理tag标签，包含新增、更新和删除三类操作，需要先进行读写权限认证。查询某个包的所有标签复用Fetch Metadata接口，如果ohpm-repo配置不支持[匿名访问](ide-ohpm-system-settings.md#section71112584105)，需要通过只读/读写Access Token进行认证；如果配置默认支持[匿名访问](ide-ohpm-system-settings.md#section71112584105)，无需进行任何认证。
8. **Versions:** 用于查看三方库版本列表，查询结果按照发布时间升序排列，以列表形式进行分页展示。可通过Options中pageNum和pageSize设置页码和每页数量。如果ohpm-repo配置不支持[匿名访问](ide-ohpm-system-settings.md#section71112584105)，或请求的仓库设置了授权可读，或请求的三方库的包权限设置了授权可读，ohpm客户端必须配置为只读或读写认证，在请求的Http Header中，通过Authorization字段携带相应的Access Token，ohpm客户端才能正确请求成功。
9. **CheckUpdate:** 用于查询当前引入的三方库是否有更新，查询结果以列表形式展示，一次最多可查询50个三方库。如果ohpm-repo配置不支持[匿名访问](ide-ohpm-system-settings.md#section71112584105)，或请求的仓库设置了授权可读，或请求的三方库的包权限设置了授权可读，ohpm客户端必须配置为只读或读写认证，在请求的Http Header中，通过Authorization字段携带相应的Access Token，ohpm客户端才能正确请求成功。

ohpm客户端在访问ohpm-repo时，支持公私钥和Access Token两种认证方式：

* 在使用公私钥认证时，ohpm客户端通过Login API从ohpm-repo获取一个Token（Token生成细节请参考Login API的具体定义），然后在调用publish，unpublish和dist-tags的API时，会在Http Header的Authorization字段携带相应的Token，该Token具有读写权限。
* 在使用Access Token认证时，需要在ohpm客户端配置[AccessToken](ide-ohpm-certification.md#section1631316181327)。Access Token 按权限范围分为两类：只读Access Token和读写Access Token。在ohpm客户端访问ohpm-repo时，Http Header的Authorization字段将携带相应的Access Token。在调用Fetch Metadata时，如果配置不支持[匿名访问](ide-ohpm-system-settings.md#section71112584105)，系统会优先识别只读Access Token，只读Access Token不存在将继续识别读写Access Token；在调用其他需读写权限API时，ohpm客户端仅识别读写Access Token。Access Token一般通过ohpm-repo管理界面生成，当然也可以使用[认证插件](ide-custom-auth-plugin.md)，将Access Token的生成代理给专门的认证服务实现，进而调用认证服务的API来完成相应的认证操作。

**说明** 

从ohpm-repo 5.4.3 Beta版本开始，Fetch Metadata API支持获取三方库的精简元数据。

从ohpm-repo 5.4.5 Beta版本开始，新增CheckUpdate API，支持查询当前引入的三方库是否有更新。

## Fetch Metadata

返回指定包的metadata元数据。

```screen
GET <router-prefix>/:group?/:package_name
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| group | string | 否 | 组织名，以@开头，比如@ohos |
| package\_name | string | 是 | 包名 (不含组织部分) |

**请求示例**（以请求一个应用内的HAR包 @test/package1 为例）**：**

```screen
请求方法：GET
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求  URL：http://myohpmrepo.com/repos/ohpm/@test/package1  
请求头：
authorization: NjJmNjFhODI3N2ZlNDUwMzlhYmUwNjQxZjQ3ZTNhZDU=
```

请求头包含两个字段，描述如下：

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| authorization | string | 是 | 填写只读或者读写AccessToken，选填项，当ohpm-repo配置不支持匿名访问时必须填写。 |
| x-ohpm-metadata-type | string | 否 | 当值为"install+v1"，返回所有精简元数据。 |
| x-ohpm-metadata-special-version | string | 否 | ohpm-repo 5.5.1版本新增。  用于返回固定版本的元数据，值支持固定版本号、latest版本号、tag版本号，示例如下。  ```screen 固定版本号： "3.0.0"  latest版本号："latest" tag版本号："tag:t310" ```  如未配置或者配置上述三种情况之外的值，返回所有元数据。 |

**响应失败示例**（以请求一个应用内的HAR包 @test/package1 为例）**：**

```screen
{
    "code": 1018,
    "message": "package not found: @test/package1"
}
```

响应失败有两个字段，描述如下：

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| code | number | 是 | 响应失败错误码 |
| message | string | 是 | 响应失败错误信息 |

**响应成功示例**（以请求一个应用内的HAR包 @test/package1 为例）：

```screen
{
  "_id": "@test/package1",
  "name": "@test/package1",
  "description": "Please describe the basic information.",
  "dist-tags": {
    "latest": "2.0.0"
  },
  "versions": {
    "1.0.0": {
      "name": "@test/package1",
      "version": "1.0.0",
      "description": "Please describe the basic information.",
      "main": "Index.ets",
      "author": {
        "name": "apple11",
        "url": "",
        "email": ""
      },
      "license": "Apache-2.0",
      "dependencies": {
      },
      "artifactType": "original",
      "_nodeVersion": "20.14.0",
      "_ohpmVersion": "ohpm-repo-5.0.3",
      "_id": "@test/package1@1.0.0",
      "dist": {
        "integrity": "sha512-UAPn6H3lsqQvwmevJSbWWv52PA8Ii6rgutLeJnVAHkNrUX2isytQ2pkzjodHuroYb64XKcwg+E6I8tUcFxwF3A==",
        "tarball": "https://myohpmrepo.com/repos/ohpm/@test/package1/-/@test/package1-1.0.0.har"
      }
    },
    "2.0.0": {
      "name": "@test/package1",
      "version": "2.0.0",
      "description": "Please describe the basic information.",
      "main": "Index.ets",
      "author": {
        "name": "apple11",
        "url": "",
        "email": ""
      },
      "license": "Apache-2.0",
      "dependencies": {
      },
      "artifactType": "original",
      "_nodeVersion": "20.14.0",
      "_ohpmVersion": "ohpm-repo-5.0.3-rc.2",
      "_id": "@test/package1@2.0.0",
      "dist": {
        "integrity": "sha512-6C47XiyVfUAljbS2d08LWEJE2dZHPFi6SNYEsR0REQVKUwlNKf6hNI8wKaI0dHCmDPhQPymOdGeTF+2E3fZWgQ==",
        "tarball": "https://10.70.95.74:8077/ohpm/@test/package1/-/@test/package1-2.0.0.har"
      }
    }
  },
  "_rev": "2",
  "time": {
    "1.0.0": "2024-06-26T14:48:17.302+08:00",
    "created": "2024-06-26T14:48:17.302+08:00",
    "modified": "2024-06-26T14:48:27.785+08:00",
    "2.0.0": "2024-06-26T14:48:27.785+08:00"
  }
}
```

如请求头通过x-ohpm-metadata-type携带value值"install+v1"即可拉取精简元数据，最外层对象只保留name、packageType、versions、dist-tags四个字段，versions版本对象层只保留name、version、dependencies、dynamicDependencies、dist、packageType、debug、\_ohpmVersion字段。上述返回成功示例如下：

```screen
{
  "name": "@test/package1",
  "dist-tags": {
    "latest": "2.0.0"
  },
  "versions": {
    "1.0.0": {
      "name": "@test/package1",
      "version": "1.0.0",
      "dependencies": {
      },
      "_ohpmVersion": "ohpm-repo-5.0.3",
      "dist": {
        "integrity": "sha512-UAPn6H3lsqQvwmevJSbWWv52PA8Ii6rgutLeJnVAHkNrUX2isytQ2pkzjodHuroYb64XKcwg+E6I8tUcFxwF3A==",
        "tarball": "https://myohpmrepo.com/repos/ohpm/@test/package1/-/@test/package1-1.0.0.har"
      }
    },
    "2.0.0": {
      "name": "@test/package1",
      "version": "2.0.0",
      "dependencies": {
      },
      "_ohpmVersion": "ohpm-repo-5.0.3-rc.2",
      "dist": {
        "integrity": "sha512-6C47XiyVfUAljbS2d08LWEJE2dZHPFi6SNYEsR0REQVKUwlNKf6hNI8wKaI0dHCmDPhQPymOdGeTF+2E3fZWgQ==",
        "tarball": "https://10.70.95.74:8077/ohpm/@test/package1/-/@test/package1-2.0.0.har"
      }
    }
  }
}
```

### metadata响应数据说明

响应数据中包含八个顶级字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| \_id | string | 包名，并用作数据库的主键ID |
| \_rev | number | 包的版本数量 |
| name | string | 包名 |
| description | string | 包的描述 |
| dist-tags | json | 包的所有标签信息 |
| versions | json | 包的所有版本数据 |
| packageType | string | 包的类型，详情见说明 |
| time | json | 包的发布时间 |

1. name: 包名，可以包含组织名称，比如@myscop/myhsplib。
2. dist-tags: 描述包的标签与包具体版本的映射关系，每一个包都有一个latest标签维护当前最大版本。
3. packageType（可选）: 描述包的类型，只有当请求的包为HSP包时，元数据中才存在packageType字段，且必须为InterfaceHar。
4. time: 维护包所有版本的发布时间，其中created表示包的首个版本发布时间，modified表示包最后一个版本的发布时间。

顶级字段中versions字段包含包的所有版本数据，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| \_id | string | 包名@包的版本号，如：@myscope/myhsplib@1.0.0 |
| \_nodeVersion | string | 发布时使用的Node.js版本 |
| \_ohpmVersion | string | 发布时使用的ohpm客户端版本 |
| name | string | 包名 |
| version | string | 包的版本号 |
| description | string | 包的描述 |
| author | json | 包的作者信息 |
| repository | string | 包的源码仓库地址 |
| license | string | 包的项目开源许可证，详情见说明 |
| packageType | string | 包的类型，详情见说明 |
| dependencies | json | 包的运行时依赖 |
| devDependencies | json | 包的开发态依赖 |
| dynamicDependencies | json | 包的动态依赖，只针对HSP包 |
| types | string | 包的类型声明文件 |
| main | string | 包的入口文件 |
| dist | json | 维护包的SSRI值及下载地址，详情见说明 |
| hspType | string | HSP包的类型，详情见说明 |
| compatibleSdkVersion | string | SDK版本 |
| compatibleSdkType | string | SDK类型 |
| nativeComponents | 数组 | native so依赖配置 |
| size | num | 包的大小 |
| fileNum | num | 包文件数量 |
| userName | string | 获取metadata数据的用户名 |
| userRole | string | 获取metadata数据的用户角色 |

1. author: 描述包的作者信息，具体为：
   * name: 必填，作者名字；
   * url: 可选，作者主页地址；
   * email: 可选，作者联系邮箱。
2. license: 当前项目的开源许可证。遵循[spdx license](https://spdx.org/licenses/)规范。许可证若为GPL，repository建议不为空。
3. packageType: 描述包的类型，只有当请求的包为HSP包时，元数据中才存在packageType字段，且必须为InterfaceHar。
4. hspType: 描述HSP包的类型，当packageType为InterfaceHar时，需要存在hspType字段，目前hspType只支持应用内HSP(bundle\_app)。
5. types: 指定包类型定义的文件名。当用ArkTs定义新的类型，需要提供给其他开发者使用，则需要指定其声明文件，一般为.d.ts和.d.ets文件，当包为HSP包时，该文件必须存在。
6. main: 指定加载的入口文件，当types不存在时，main必须存在。
7. dist: 维护包的SSRI值及下载地址，具体字段有：
   * integrity: .har文件的[SSRI](https://w3c.github.io/webappsec/specs/subresourceintegrity/)值，用于完整性校验；
   * tarball: .har文件的下载地址;
   * integrity\_hsp: 当包hspType为bundle\_app时，会存在.hsp后缀的文件，该字段为的.hsp文件的SSRI值；
   * resolved\_hsp: .hsp文件的下载地址。

## Login

客户端登录，获得上传包，下架包和编辑标签tag时所需的token。

```screen
POST <router-prefix>/login
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| ohpm-repo仓库地址 | string | 是 | 实际搭建的ohpm-repo仓库域名或IP地址 |
| repo\_name | string | 是 | 指定访问的仓库名称 |

**请求示例**：

```screen
请求方法：POST
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/login  
请求头：
command: login；
请求体（json格式内容）：
{
  "publishId": "95115BAFDE",
  "timestamp": 1702088629606,
  "nonce": "e3b3d53f91d0488f9838c86e306ca9f5",
  "signature": "qXYUnUK8Quy95a...",
  "version": "v1"
}
```

请求头包含四个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| command | string | 命令的名称，选填 |

请求体包含五个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| version | string | 协议版本，必选 |
| publishId | string | 发布码，必选 |
| timestamp | number | 发布时间戳，必选 |
| nonce | string | 随机数，必选 |
| signature | string | 签名值，具体见下述说明，必选 |

1、publishId: 由ohpm-repo私仓生成的发布码，与用户绑定，每个用户的发布码是唯一的，在客户端的.ohpmrc文件中通过publish\_id配置；

2、timestamp: 时间戳，单位为毫秒；

3、nonce: 客户端在登录时动态生成的uuidv4随机数；

4、signature: 客户端在登录时，将协议版本、发布码、发布时间戳和随机数以v{version}-{publishId}-{timestamp}-{nonce}格式组合而成，并使用私钥经RSA-SHA256算法签名而生成。

**响应成功示例：**

```screen
{
  "success": true,
  "token": "7100c3f38dddf3cf8234...."
}
```

成功响应体包含2个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| success | boolean | 响应是否成功，值为true |
| token | string | 认证成功返回的token值 |

**响应失败示例：**

```screen
{
    "success": false,
    "error": "The timestamp is expired"
}
```

失败响应体包含2个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| success | boolean | 响应是否成功，值为false |
| error | string | 认证失败返回的错误原因 |

**说明** 

token: 使用公私钥认证时，ohpm-repo生成的认证信息。认证信息必须验证有效，才有权限执行上传包、下架包和编辑标签tag等操作。

## Publish

### 上传一个HAR/HSP包到ohpm-repo私仓中

```screen
PUT <router-prefix>/:package_name
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| package\_name | string | 是 | 包名 |

**说明** 

若包名中包含组织名，则package\_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package\_name为@myscope%2fmypkg。

请求示例（以上传一个应用内的HSP包@myscope/myhsppkg为例）：

```screen
请求方法：PUT
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/@myscope%2fmypkg  
请求头：
command: publish
Authorization：<token>
请求体（包的metadata数据，由ohpm客户端生成）：
{
  "_id": "@myscope/myhsppkg",
  "name": "@myscope/myhsppkg",
  "packageType": "InterfaceHar",
  "description": "Please describe the basic information.",
  "dist-tags": {
    "latest": "1.0.4"
  },
  "versions": {
    "1.0.4": {
      "name": "@myscope/myhsppkg",
      "version": "1.0.4",
      "description": "Please describe the basic information.",
      "author": {
        "name": "fsq",
        "url": "",
        "email": ""
      },
      "license": "Apache-2.0",
      "packageType": "InterfaceHar",
      "dependencies": {
        "pkga": "1.0.0",
        "pkgb": "1.0.0"
      },
      "types": "Index.d.ets",
      "_nodeVersion": "16.20.1",
      "_ohpmVersion": "1.4.0",
      "_id": "@myscope/myhsppkg@1.0.4",
      "dist": {
        "integrity": "sha512-0bHCBS2JtlyX7Gq5q6tbO2eRRbj0RO2cAAagC/K6/zmDZHPGrnIScDkD3Yjip8I/YWq7VbY7HYlHXtcLApILVg==",
        "tarball": "https://localhost:8081/repos/ohpm/@myscope/myhsppkg/-/@myscope/myhsppkg-1.0.4.har",
        "integrity_hsp": "sha512-3B7KlJFEHuQ9X+Zxl+oRVIL8CCczaPu2nEGQvXrULrViXuY80Ld2CnkQEVFfd/eZK6DNAFTS1wBhqOTLYtOqow=="
      }
    }
  },
  "_attachments": {
    "@test/ohpmhsplib-1.0.4.har": {
      "content_type": "application/octet-stream",
      "data": "H4sIAAAAAAAACu1ZUU...",
      "length": 858
    },
    "@test/ohpmhsplib-1.0.4.hsp": {
      "content_type": "application/octet-stream",
      "data": "UEsDBAoAAAgAAAAAIU5v...",
      "length": 29185
    }
  },
  "hspType": "bundle_app"
}
```

请求头包含五个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| command | string | 命令的名称，选填 |
| Authorization | string | 认证信息，AccessToken的值或者调用login接口的token值，必填 |

请求体数据中包含八个顶级字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| \_id | string | 包名，并用作数据库的主键ID |
| name | string | 包名 |
| description | string | 包的描述 |
| dist-tags | json | 包的所有标签信息 |
| versions | json | 包的所有版本数据 |
| packageType | string | 包的类型，详情见说明 |
| \_attachments | json | 待发布包的包数据信息 |
| hspType | json | hsp包的类型 |

**说明** 

1. 当上传的包为应用内HSP包时，包格式为tgz格式，内部包含.har及.hsp两个文件，且在元数据的\_attachments部分会包含这两个文件。
2. 当上传的包为HAR包，包格式为.har格式。
3. 当上传HSP包时，提交的元数据中会存在packageType字段，且为InterfaceHar。
4. 当上传的包为应用内HSP包时，提交的元数据中version的dist域中存在integrity\_hsp字段，表示HSP部分的SSRI值。

**成功响应体示例：**

```screen
{
    "code": 200,
    "message": "success"，
}
```

**失败响应体示例：**

```screen
{
    "success": false,
    "error": "<error message>"，
 }
```

### 流式上传一个HAR/HSP到ohpm-repo

ohpm客户端（5.0.1版本）和ohpm-repo（5.0.1版本）开始支持使用流式上传，当上传的三方包大小超过阈值（默认5M，可在.ohpmrc中自定义配置）时，ohpm会优先调用流式上传接口进行上传。

```screen
POST <router-prefix>/stream/:package_name
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| package\_name | string | 是 | 包名。若包名中包含组织名，则package\_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package\_name为@myscope%2fmypkg。 |

**请求示例**（以上传一个应用内的HSP包@myscope/myhsppkg为例）：

```screen
请求方法：POST
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/stream/@myscope%2fmypkg  
请求头：
command: publish
Authorization：<token>
请求体：formData数据格式，由两部分组成：
1）metadata=<file.json>：包的元数据
2）pkg_stream=<@hsp.tgz;application/octet-stream>：待上传包的文件流数据
```

请求示例中请求体的包元数据内容如下所示：

```screen
{
  "_id": "@myscope/myhsppkg",
  "name": "@myscope/myhsppkg",
  "packageType": "InterfaceHar",
  "description": "Please describe the basic information.",
  "dist-tags": {
    "latest": "1.0.4"
  },
  "versions": {
    "1.0.4": {
      "name": "@myscope/myhsppkg",
      "version": "1.0.4",
      "description": "Please describe the basic information.",
      "author": {
        "name": "fsq",
        "url": "",
        "email": ""
      },
      "license": "Apache-2.0",
      "packageType": "InterfaceHar",
      "dependencies": {
        "pkga": "1.0.0",
        "pkgb": "1.0.0"
      },
      "types": "Index.d.ets",
      "_nodeVersion": "16.20.1",
      "_ohpmVersion": "1.4.0",
      "_id": "@myscope/myhsppkg@1.0.4",
      "dist": {
        "integrity": "sha512-0bHCBS2JtlyX7Gq5q6tbO2eRRbj0RO2cAAagC/K6/zmDZHPGrnIScDkD3Yjip8I/YWq7VbY7HYlHXtcLApILVg==",
        "tarball": "https://localhost:8081/repos/ohpm/@myscope/myhsppkg/-/@myscope/myhsppkg-1.0.4.har",
        "integrity_hsp": "sha512-3B7KlJFEHuQ9X+Zxl+oRVIL8CCczaPu2nEGQvXrULrViXuY80Ld2CnkQEVFfd/eZK6DNAFTS1wBhqOTLYtOqow=="
      }
    }
  },
  "hspType": "bundle_app"
   "pkg": "D:\\basicData\\har\\package.tgz",
   "isTgz": true
}
```

请求头包含五个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| command | string | 命令的名称，选填 |
| Authorization | string | 认证信息，AccessToken的值或者调用login接口的token值，必填 |

请求体的metadata数据中包含九个顶级字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| \_id | string | 包名，并用作数据库的主键ID |
| name | string | 包名 |
| description | string | 包的描述 |
| dist-tags | json | 包的所有标签信息 |
| versions | json | 包的所有版本数据 |
| packageType | string | 包的类型，详情见说明 |
| hspType | json | hsp包的类型 |
| pkg | string | 记录上传包的路径 |
| isTgz | boolean | 记录是否是tgz包 |

**说明** 

1. 当上传的包为应用内HSP包时，包格式为tgz格式，内部包含.har及.hsp两个文件。
2. 当上传的包为HAR包，包格式为.har格式。
3. 当上传HSP包时，提交的元数据中会存在packageType字段，且为InterfaceHar。
4. 当上传的包为应用内HSP包时，提交的元数据中version的dist域中存在integrity\_hsp字段，表示HSP部分的SSRI值。

**成功响应体示例：**

```screen
{
    "code": 200,
    "message": "success"
}
```

**失败响应体示例：**

```screen
{
    "success": false,
    "error": "<error message>"
 }
```

## Unpublish

从ohpm-repo中下架一个HAR/HSP包 （下架一个包的某个版本，或是整个包）。

```screen
DELETE <router-prefix>/:package_name
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| package\_name | string | 是 | 包名 |

**说明** 

1. 若包名中包含组织名，则package\_name为包名进行url编码后的结果，比如：当包名为@myscope/myhsppkg时，package\_name为@myscope%2fmyhsppkg。
2. 若指定具体版本需要在请求体中加上<version>部分，比如：{"version":"1.0.0"}。
3. 若不指定具体版本，则表示下架该包所有版本。

请求示例：

```screen
请求方法：DELETE
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/@myscope%2fmyhsppkg  
请求头：
command: unpublish
Authorization：<token>
请求体：
{"version":"1.0.0"}
```

请求头包含五个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| command | string | 命令的名称，选填 |
| Authorization | string | 认证信息，AccessToken的值或者调用login接口的token值，必填 |

**成功响应体示例：**

```screen
{
    "code": 200,
    "message": "success"
}
```

**失败响应体示例：**

```screen
{
    "success": false,
    "error": "<error message>"
 }
```

## Ping

检测与ohpm-repo仓库的网络连通性。

```screen
GET <router-prefix>/-/ping
```

请求示例：

```screen
请求方法：GET
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/-/ping
```

响应成功示例：

```screen
{
    "code": 200,
    "message": "success"
}
```

失败响应体示例：

```screen
{
    "success": false,
    "error": "<error message>"
 }
```

## DistTags

### 新增tag

为包添加tag。

```screen
POST <router-prefix>/-/package/:package_name/dist-tags/:tag
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| package\_name | string | 是 | 包名 |
| tag | string | 是 | 标签名 |

**说明** 

若包名中包含组织名，则package\_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package\_name为@myscope%2fmypkg。

请求示例（为包@myscope/myhsppkg@1.0.0增加标签（tag）test）：

```screen
请求方法：POST
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/-/package/@myscope%2fmypkg/dist-tags/test
请求头：
command: dist-tags
Authorization：<token>
请求体：
{"version":"1.0.0"}
```

请求头包含五个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| command | string | 命令的名称，选填 |
| Authorization | string | 认证信息，AccessToken的值或者调用login接口的token值，必填 |

响应成功示例：

```screen
{
    "code": 200,
    "message": "success"
}
```

失败响应体示例：

```screen
{
    "success": false,
    "error": "<error message>"
 }
```

### 更新tag

修改包tag对应的版本号。

```screen
PUT <router-prefix>/-/package/:package_name/dist-tags/:tag
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| package\_name | string | 是 | 包名 |
| tag | string | 是 | 标签名 |

请求示例（为包@myscope/myhsppkg修改标签（tag）test对应版本号为2.0.0）：

```screen
请求方法：PUT
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/-/package/@myscope%2fmypkg/dist-tags/test
请求头：
command: dist-tags
Authorization：<token>
请求体：
{"version":"2.0.0"}
```

请求头包含五个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| command | string | 命令的名称，选填 |
| Authorization | string | 认证信息，AccessToken的值或者调用login接口的token值，必填 |

**响应成功示例：**

```screen
{
    "code": 200,
    "message": "success"
}
```

**失败响应体示例：**

```screen
{
    "success": false,
    "error": "<error message>"
 }
```

### 删除tag

删除包的tag。

```screen
DELETE <router-prefix>/-/package/:package_name/dist-tags/:tag
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| package\_name | string | 是 | 包名 |
| tag | string | 是 | 标签名 |

**请求示例**（删除包@myscope/myhsppkg的标签（tag）test）：

```screen
请求方法：DELETE
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/-/package/@myscope%2fmypkg/dist-tags/test
请求头：
command: dist-tags
Authorization：<token>
```

请求头包含五个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| command | string | 命令的名称，选填 |
| Authorization | string | 认证信息，AccessToken的值或者调用login接口的token值，必填 |

**响应成功示例：**

```screen
{
    "code": 200,
    "message": "success"
}
```

**失败响应体示例：**

```screen
{
    "success": false,
    "error": "<error message>"
 }
```

## Versions

用于查看三方库版本列表，查询结果按照发布时间升序排列，以列表形式进行分页展示。

```screen
GET <router-prefix>/:group?/:package_name/versions?pageNum=1&pageSize=10
```

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| group | string | 否 | 组织名，以@开头，比如@ohos |
| package\_name | string | 是 | 包名 (不含组织部分) |
| pageNum | number | 否 | 页码，取值范围：[1, 10000] |
| pageSize | number | 否 | 每页的版本数量，取值范围：[1, 500] |

**说明** 

若包名中包含组织名，则package\_name为包名进行url编码后的结果，比如：当包名为@myscope/mypkg时，package\_name为@myscope%2fmypkg。

请求示例（以查看@myscope/myhsppkg包中的版本为例）：

```screen
请求方法：GET
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
请求 URL：http://myohpmrepo.com/repos/ohpm/@myscope%2fmypkg/versions?pageNum=1&pageSize=10
请求头：
authorization: NjJmNjFhODI3N2ZlNDUwMzlhYmUwNjQxZjQ3ZTNhZDU=
```

请求头包含一个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| authorization | string | 填写只读或者读写AccessToken，选填项，当ohpm-repo配置不支持匿名访问时必须填写。 |

**响应失败示例**（以请求一个应用内的HAR包 @test/package1 为例）**：**

```screen
{
    "code": 1018,
    "message": "package not found: @test/package1"
}
```

响应失败有两个字段，描述如下：

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| code | number | 是 | 响应失败错误码 |
| message | string | 是 | 响应失败错误信息 |

**响应成功示例**：

```screen
{
    "code": 200,
    "body": {
        "total": 2,
        "pageNum": 1,
        "pageSize": 10,
        "rows": ["1.0.1","1.0.2"],
        "pages": 1
    } 
}
```

**失败响应体示例**：

```screen
{
    "code": 404,
    "error": "<error message>"
 }
```

## CheckUpdate

用于查询当前引入的三方库是否有更新，查询结果会过滤掉不存在的包以列表形式展示，一次最多可查询50个库。

```screen
POST <router-prefix>/checkUpdate
```

请求体body为一个array数组，数组最大长度为50，body的item是一个json对象，包含五个字段，描述如下：

| 属性 | 类型 | 必填项 | 描述 |
| --- | --- | --- | --- |
| packageName | string | 是 | 包名 (含组织部分) |
| moduleName | string | 是 | 模块名，用来标识当前这个请求体中的包名来源于哪个模块 |
| dependencyConfig | string | 是 | 模块中包配置的依赖版本，仅支持远程依赖，长度为(0，128]。  远程依赖的格式有：   * 确切版本号：x.x.x * 更新补丁版本：~x.x.x、~x.x * 更新次版本：^x.x.x * 通配符：\*、x.x.\* * 版本号范围：>1.0.0、<=2.0.0、1.2.0 - 2.0.0 * 最新版本：latest * 标签版本：tag:beta |
| installedVersion | string | 否 | 当前已安装依赖的版本，如未安装，可为空 |
| depth | number | 是 | 标识当前包是否为直接依赖，当前只支持直接依赖，固定值为0 |

请求示例（以查看@myscope/myhsppkg包的版本更新为例）：

```screen
请求方法：post
// http://myohpmrepo.com：ohpm-repo仓库地址，开发过程中需要替换为实际搭建的ohpm-repo仓库域名或IP地址。
// repos：固定字段。
// ohpm：指定访问的仓库名称，开发过程中需要替换为实际使用的仓库。
// checkUpdate：固定字段。
请求 URL：http://myohpmrepo.com/repos/ohpm/checkUpdate
请求头：
Authorization: NjJmNjFhODI3N2ZlNDUwMzlhYmUwNjQxZjQ3ZTNhZDU=
请求体：
[
    {
        "packageName":"@myscope/myhsppkg",
        "moduleName":"modulea",
        "dependencyConfig":"*",
        "installedVersion":"1.0.0",
        "depth":0
    }
]
```

请求头包含一个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| Authorization | string | 填写只读或者读写AccessToken，选填项。  ohpm-repo不支持匿名访问时，必填项。 |

**响应成功示例**：

```screen
{
    "code": 200,
    "body": [
        {
            "packageName": "@myscope/myhsppkg",
            "depth": 0,
            "moduleName": "modulea",
            "installedVersion": "1.0.0",
            "wantedVersion": "2.0.0",
            "latestVersion": "2.0.0",
            "updateType": "major",
            "description": "major update",
            "dependentPackageName": "",
            "homePage": "",
            "recommend": [],
            "security": []
        }
    ]
}
```

响应体包含两个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| code | string | 状态码 |
| body | array | 对应的包版本更新信息列表 |

body的item是一个json对象，包含十二个字段，描述如下：

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| packageName | string | 包名(含组织部分) |
| depth | string | 标识当前包是否为直接依赖，当前只支持直接依赖，固定值为0 |
| moduleName | string | 模块名，用来标识当前这个请求体中的包名来源于哪个模块 |
| installedVersion | string | 当前已安装依赖的版本 |
| wantedVersion | string | 根据依赖配置 匹配到的版本 |
| latestVersion | string | 当前这个包的最新版本 |
| updateType | string | 更新类型 |
| description | string | 更新描述词 |
| dependentPackageName | string | 预留字段，默认为空 |
| homePage | string | 包仓库地址，私仓不涉及，固定为"" |
| recommend | array | 优选推荐包，私仓不涉及，固定为[] |
| security | array | 该包当前使用版本（installVersion）的安全风险信息，私仓不涉及，固定为[] |

**响应失败示例****：**

```screen
{
    "code": 1001,
    "error": "ModuleName verification failed"
}
```

## 仓库响应码说明

| 响应码 | 范围 | 说明 |
| --- | --- | --- |
| 200 | 仓库所有接口 | 成功 |
| 400 | 仓库所有接口 | 登录失败、未知错误失败 |
| 401 | Fetch Metadata、Publish、Unpublish、DistTags、Versions、CheckUpdate | 客户端传参校验失败、认证失败 |
| 404 | 访问仓库不存在的接口 | 接口不存在 |
| 500 | 仓库所有接口 | 服务器内部错误 |
| 598 | Publish | 当仓库上传接口返回的响应状态码为598时，ohpm 5.0.1及以上版本会尝试去重新上传 |

**注意** 

由于[流式上传接口](ide-interface-protocol.md#section08863329310)在ohpm 5.0.1版本才开始支持，当ohpm调用该接口时，若返回的响应状态码为404时，ohpm客户端会再次调用[上传接口](ide-interface-protocol.md#section444511511524)上传。为了保证与ohpm客户端的兼容性，请确保当访问仓库不存在的接口仓库的响应状态码为404。
