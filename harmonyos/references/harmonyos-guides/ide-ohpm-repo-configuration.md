---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration
title: 配置文件
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 配置文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:39+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:5d920edd7bf15cdf27682294d5e2f979e4113672d39f605ac562d5cf94899a7a
---

config.yaml是ohpm-repo的重要文件，可以在其中修改默认参数配置，启动插件和扩展功能。ohpm-repo私仓解压目录中的conf目录下带有一个默认配置文件config.yaml，ohpm-repo执行install命令时默认读取该文件。

说明

**ohpm-repo成功启动后修改配置文件方法**：

* 首次启动ohpm-repo时执行**install**命令时已指定配置文件：找到指定的配置文件进行文件内容修改，然后重新执行install指定修改后的配置文件，再执行start启动ohpm-repo。
* 首次启动ohpm-repo时执行**install**命令未指定配置文件：默认使用ohpm-repo压缩包解压路径下conf目录中的配置文件，修改该文件内容，然后重新执行install和start操作。

## 默认配置

```
1. ##### server configuration section #####
2. listen: localhost:8088        # 建议修改为具体的ip/域名
3. # listen:
4. # - localhost:8088            # 监听本机环回地址
5. # - http://localhost:8088     # 监听本机环回地址
6. # - 0.0.0.0:8088              # 监听本机所有地址 (INADDR_ANY)
7. # 协议可配置 http 或者 https，默认为 http
8. # port: 1-65535(Windows系统)/ 1024-65535(Linux或Mac系统）

10. # 可选 (listen 为 https 协议时必须配置)
11. https_key: ''                 # https 服务使用的 key 的路径  (不配置默认为'')
12. https_cert: ''                # https 服务使用的 crt 的路径  (不配置默认为'')

14. ##### server deploy root section #####
15. deploy_root: ''                # 安装根目录，只支持绝对路径，且目录必须存在

17. ##### server numeric limit section #####
18. max_package_size: 500          # 上传包大小限制，单位是MB (0, 500]，不配置或配置为0默认为 500
19. max_extract_size: 800          # 压缩包解压后大小限制，单位是MB ，不配置或配置为0默认为 800
20. max_extract_file_num: 30000    # 压缩包解压后文件个数限制，不配置或配置为0默认为30000个
21. user_rate_limit: 100           # 用户访问频率控制，单位是次/小时 (0, 10000]，不配置或配置为0默认为 100
22. fetch_timeout: 60              # 请求/响应的超时时间，单位是秒 (0, 3600]，不配置或配置为0默认为 60
23. keep_alive_timeout: 60         # TCP 保持连接的超时时间，单位是秒 (0, 3600]，不配置或配置为0默认为 60
24. api_timeout: 60                # api超时时间，单位是秒(0, 3600]，不配置或配置为0默认为 60
25. upload_api_timeout: 300        # 上传三方包api超时时间，单位是秒(0, 3600]，不配置或配置为0默认为 300
26. upload_lock_hour: 24           # 下架某一三方包所有版本后，限时禁止同名三方包上传，单位是小时 (0, 168]，不配置或配置为0默认为 24
27. upload_max_times: 100          # 单用户24小时内上传次数限制 (0, 100000]，不配置或配置为0默认为 100
28. operation_log_retention: 100   # 数据库中操作日志保留时间，单位是天，不配置或配置为0默认为 100

30. ##### metadata storage section #####
31. ## 数据存储类型 filedb 和 mysql 二选一，不可都配置
32. db:                         # 必须用 yaml 数组形式写法
33. type: filedb
34. config:                   # 如果想修改存储路径且保留旧的数据，则需要把旧路径下的数据文件迁移至新路径
35. path: ./db              # 本地数据存储路径，不配置默认为<deploy_root>/db;

37. #db:                        # 必须用yaml数组形式写法
38. #  type: mysql
39. #  config:
40. #    host: "localhost"      # 数据库主机地址
41. #    port: 3306             # 数据库端口 (0,65535]
42. #    username: tctAdmin         # 数据库的用户名
43. #    password: "password"   # 数据库的用户密码（请配置明文, 最终在部署目录中会转换为密文）
44. #    database: "repo"       # 数据库名

46. ##### storage section #####
47. ## 文件存储类型fs,sftp 和 custom 三选一，不可多选。

49. store:                               # 必须用 yaml 数组形式写法
50. type: fs
51. config:                            # 上传资源后如若要修改存储路径，则需要把旧路径下的数据迁移至新路径中
52. path: ./storage                  # 已上架三方库存储路径，不配置默认为 <deploy_root>/storage;
53. #server: http://localhost:8088   # 仓库下载链接地址，不配置取默认值

55. # 文件存储类型为 sftp 时，最多配置三个 sftp
56. #store:                               # 必须用 yaml 数组形式写法
57. #  type: sftp                         # 当且仅当 db 的类型为 mysql 时，store 的类型才能为 sftp
58. #  config:
59. #    location:
60. #      -
61. #        name: test_one_sftp          # 主机名字不能与其他sftp配置重复
62. #        host: "localhost"            # 主机地址
63. #        port: 22                     # 主机端口 (0,65535]
64. #        read_username: "read"        # 主机有读权限的用户名字
65. #        read_password: "password"    # 主机有读权限的用户密码（请配置明文, 最终在部署目录中会转换为密文）
66. #        write_username: "write"      # 主机有写权限的用户名字
67. #        write_password: "password"   # 主机有写权限的用户密码（请配置明文, 最终在部署目录中会转换为密文）
68. #        path: /source22              # 相对 sftp 根目录的文件路径，仅限/开头，且路径文件夹必须存在
69. #      -
70. #        name: test_two_sftp
71. #        host: "localhost"
72. #        port: 24
73. #        read_username: "read"
74. #        read_password: "password"
75. #        write_username: "write"
76. #        write_password: "password"
77. #        path: /source24
78. #    #server: http://localhost:8088   # 仓库下载链接地址，不配置取默认值

80. #store:
81. #  type: custom                                            # custom是自定义存储插件类型，自定义存储插件开发流程见指导文档
82. #  config:
83. #    export_name: CustomStorage                            # 插件export的类名
84. #    plugin_path: plugins/CustomStorage.js                 # 插件的绝对路径或者相对于ohpm-repo软件包的路径，建议将插件放在软件包的plugins目录下
85. #    custom_field: "test"                                  # 自定义字段，通过引入libs/common/getStorageConfigInfo.js的getStorageConfigInfo方法获取自定义字段的值
86. #    #server: http://localhost:8088                        # 仓库下载链接地址，不配置取默认值

88. ##### 是否使用反向代理 #####
89. # 可选项:true,false, 默认：false。如果使用反向代理，需要配置为true，客户端IP地址将从请求头中的x-forwarded-for字段获取
90. use_reverse_proxy: false

92. ##### uplink section #####
93. uplink_cache_path: ./uplink      # 缓存路径，不配置默认为 <deploy_root>/uplink
94. uplink_cache_time: 168           # 远程包 metadata 缓存时间，单位为小时，默认 168 小时，取值范围为 (0, 8760]

96. ##### log section #####
97. logs_path: ./logs                # 日志路径，不配置默认为 <deploy_root>/logs

99. ##### log level section #####
100. # 日志级别: 级别由低到高分别是 all、trace、debug、info、warn、error、fatal、mark、off
101. # run，operate 和 access 不配置或者配置错误，默认为 info
102. loglevel_run: info
103. loglevel_operate: info
104. loglevel_access: info

106. ##### auth plugin section #####
107. # 可选项，自定义认证插件配置
108. #auth_plugin:
109. #  name: CustomAuth              # 认证插件的名字
110. #  path: plugins/CustomAuth.js   # 插件的绝对路径或者相对于ohpm-repo软件包的路径，建议将插件放在软件包的plugins目录下

112. ##### fieldCheck plugin section #####
113. # 可选项，自定义元数据规则检验插件配置
114. #field_check_plugin:
115. #  config_file_path:  plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json  # 字段校验配置文件的绝对路径或者相对于ohpm-repo软件包的路径，建议将文件放在软件包的plugins/fieldCheckPlugin目录下
116. #  check_func_dir: plugins/fieldCheckPlugin                                          # 字段校验函数文件所在目录的绝对路径或者相对于ohpm-repo软件包的路径，建议将目录设置为plugins/fieldCheckPlugin文件夹

118. ##### content check plugin #####
119. # 可选项，包内容规则检测插件配置
120. #content_check_plugin:
121. # 该校验要求环境变量中有ark_disasm可执行文件、tar命令行工具
122. # 检查范围：上架的字节码har、hsp
123. #  name: 'OHMUrlCheck'

125. ##### compatibleSdkVersion等兼容性字段检测日志等级 #####
126. # 可选值：close、info、warn、error，默认：warn
127. compability_log_level: warn

129. ##### 是否允许下架被其他组件依赖的包 #####
130. # 可选项:true,false, 默认：false
131. allow_remove_depended_packages: false
```

## 配置项说明

### listen

格式为三段式，即<proto>://<host>:<port>，其中<proto>可以不填，默认为http，如：

* 监听本机回环地址（默认）：

  ```
  1. listen: localhost:8088
  2. # 或 listen: http://localhost:8088
  ```
* 监听具体地址（建议）：

  ```
  1. listen: https://<ohpm-repo部署机器ip>:8088
  ```
* 监听所有地址（当选择监听所有地址时，配置项[store](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_store)中server值必须配置）：

  ```
  1. listen: 0.0.0.0:8088
  2. # 或 listen: http://0.0.0.0:8088
  ```

注意

listen值建议监听具体的地址。proto支持http和https协议，支持缺省，缺省时默认为http。为了确保ohpm-repo链接的安全，建议选择使用https协议，如果配置为https协议，则需要完善[https](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_https)相关配置。

### https

当配置[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)时选择使用https协议，则需要配置https\_key和https\_cert：

* https\_key：ssl证书私钥文件。
* https\_cert：ssl证书文件。

参考配置如下：

```
1. https_key: ./ssl/server.key
2. https_cert: ./ssl/server.crt
```

说明

生产环境必须使用受信任CA颁发的证书，避免因使用自签名证书导致浏览器安全警告。

### deploy\_root

ohpm-repo的部署目录，存储运行时生成的文件数据。

* 如果<deploy\_root>字段为空，则默认路径为：

  windows系统: ~/AppData/Roaming/Huawei/ohpm-repo

  其他操作系统：~/ohpm-repo
* 如果<deploy\_root>字段不为空，则路径必须为**绝对路径**，且路径所指向文件夹**必须存在**。
* 该路径不允许配置为ohpm-repo安装包解压根目录。

参考配置如下：

```
1. deploy_root: ''
```

### server

服务相关配置，具体为：

* **max\_package\_size**: 上传包大小限制，单位为MB， 不配置或配置为0取默认值500MB，取值范围为 (0, 500] 。
* **max\_extract\_size**: 压缩包解压后大小限制，单位为MB，不配置或配置为0取默认值800MB。
* **max\_extract\_file\_num**: 压缩包解压后文件个数限制，不配置或配置为0取默认值30000个。
* **user\_rate\_limit**: 用户访问频率控制，单位为次/秒，不配置或配置为0取默认值100次/秒，取值范围为 (0, 10000]。
* **fetch\_timeout**: 当使用[uplink](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_uplink)时，请求uplink数据的请求/响应超时时间，单位为秒，不配置或配置为0取默认值60秒，取值范围为 (0, 3600]。
* **keep\_alive\_timeout**: TCP 保持连接的超时时间，单位为秒，不配置或配置为0取默认值60秒，取值范围为 (0, 3600]。
* **api\_timeout**: 接口请求与响应超时时间，单位为秒，不配置或配置为0取默认值60秒，取值范围(0, 3600]。
* **upload\_api\_timeout**: 上传三方包接口请求与响应超时时间，单位为秒，不配置或配置为0取默认值300秒，取值范围(0, 3600]。
* **upload\_lock\_hour**: 下架某个三方包所有版本后，限时禁止同名三方包上传，单位为小时，不配置或配置为0取默认值24小时，取值范围为 (0, 168]。
* **upload\_max\_times**: 单用户24小时内上传次数限制，不配置或配置为0取默认值100次，取值范围为 (0, 100000]。
* **operation\_log\_retention**：数据库中操作日志保留时间，单位是天，不配置或配置为0取默认值100天。

参考配置如下：

```
1. max_package_size: 500
2. max_extract_size: 800
3. max_extract_file_num: 30000
4. user_rate_limit: 100
5. fetch_timeout: 60
6. keep_alive_timeout: 60
7. api_timeout: 60
8. upload_api_timeout: 300
9. upload_lock_hour: 24
10. upload_max_times: 100
11. operation_log_retention: 100
```

注意

db是元数据存储的配置项，store是文件存储的配置项。db支持fileDB本地存储和mysql数据库存储；store支持file storage存储，sftp存储和custom storage 自定义插件存储。db和store不能随意搭配，需要符合表1的匹配规范：

**表1** db配置项与store配置项的搭配选择

| db：元数据存储 | **与db所适配的store：三方包文件存储** |
| --- | --- |
| filedb | file storage |
| mysql(ohpm-repo 1.1.0开始支持） | file storage，sftp storage(ohpm-repo 1.1.0开始支持），custom storage(ohpm-repo 2.2.0开始支持） |

### db

ohpm-repo运行过程产生的用户信息，运行状态等元数据存储配置，支持本地磁盘存储filedb和mysql数据库存储。

**本地磁盘存储**

默认使用本地磁盘存储，配置如下：

* type: 存储插件名称，为filedb。
* config: 插件配置，具体为：
  + path: 数据库文件存储地址，默认值为./db，支持相对和绝对路径配置，当配置为相对路径时，则以[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)为根目录。

说明

如果想修改数据库文件存储路径同时保留旧的数据，则需要把旧路径下的数据文件迁移至新路径。

参考配置如下：

```
1. db:
2. type: filedb
3. config:
4. path: ./db
```

**mysql存储**

* type: 插件名称，配置为mysql。
* config: 插件配置，具体为：
  + host: 数据库主机地址。
  + port: 数据库端口。
  + username: 数据库的用户名。
  + password: 数据库的用户密码（请配置明文, 最终在部署目录中会转换为密文）。
  + database: 数据库名。

参考配置如下：

```
1. db:
2. type: mysql
3. config:
4. host: "localhost"
5. port: 3306
6. username: "tctAdmin"
7. password: "password"
8. database: "repo"
```

注意

为了避免潜在的安全风险，建议使用非最高权限的数据库账户进行连接。

### store

三方库及其元数据等资源文件存储配置，支持本地磁盘存储，sftp存储和自定义插件存储。

**本地磁盘存储**

默认使用本地磁盘存储文件，具体配置为：

* type: 插件名称，为fs。
* config: 插件配置，具体为：
  + path: 存储根目录路径，默认为./storage，支持相对和绝对路径配置，当配置为相对路径时，则以[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)为根目录。
  + server: 仓库内容的下载地址，当[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0且本机存在多个网络接口时，**必须配置**。
    - server的格式如下：<[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的proto>://<host>:<[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的port>；
    - 当配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host不为0.0.0.0时，则server**默认**取listen的完整格式，例如listen为127.0.0.1:8088，故server默认值为http://127.0.0.1:8088；
    - 当配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0时，如果本机仅存在一个网络接口，则server中的host默认为本机网络接口的ipv4地址；如果本机存在多个网络接口，则server中的host默认为本机获取到的第一个网络接口的ipv4地址，建议手动修改host为指定的本机ip/域名，例如listen为0.0.0.0:8088，故server需配置为http://<本机ip/域名>:8088；
    - 如果需要通过反向代理来访问ohpm-repo服务，则该字段须配置为反向代理服务器的域名地址，且需要配置[use\_reverse\_proxy](ide-ohpm-repo-configuration.md#section1074004784011)值为true。

注意

上传资源后如若要修改存储路径，则需要把旧路径下的数据迁移至新路径中。

参考配置如下：

```
1. store:
2. type: fs
3. config:
4. path: ./storage
5. #server: http://localhost:8088
```

**sftp 存储**

支持使用sftp存储文件，仅当数据存储为mysql存储时才能使用sftp存储，具体配置为：

* type: 插件名称，其名称为sftp。
* config: 插件配置。
  + location: 支持配置最多3个sftp服务，必须用yaml的数组形式写法，详细配置如下；
    - name: sftp服务名，名字不能与其他sftp配置重复。
    - host: sftp服务主机地址。
    - port：sftp服务端口。
    - read\_username：有读权限的用户名。
    - read\_password：有读权限的用户密码（请配置明文, 最终在部署目录中会转换为密文)。
    - write\_username：有写权限的用户名。
    - write\_password：有写权限的用户密码（请配置明文, 最终在部署目录中会转换为密文)。
    - path：相对 sftp 根目录的文件路径，仅限/开头，且路径所指向的文件夹必须存在。
  + server: 仓库内容的下载地址，当[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0且本机存在多个网络接口时，**必须配置**。
    - server的格式如下：<[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的proto>://<host>:<[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的port>
    - 当配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host不为0.0.0.0时，则server**默认**取listen的完整格式，例如listen为127.0.0.1:8088，故server默认值为 http://127.0.0.1:8088；
    - 当配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0时，如果本机仅存在一个网络接口，则server中的host默认为本机网络接口的ipv4地址；如果本机存在多个网络接口，则server中的host默认为本机获取到的第一个网络接口的ipv4地址，建议手动修改host为指定的本机ip/域名，例如listen为0.0.0.0:8088，故server需配置为http://<本机ip/域名>:8088；
    - 如果需要通过反向代理来访问ohpm-repo服务，则该字段须配置为反向代理服务器的域名地址，且需要配置[use\_reverse\_proxy](ide-ohpm-repo-configuration.md#section1074004784011)值为true。

参考配置如下：

```
1. store:
2. type: sftp
3. config:
4. location:
5. -
6. name: test_one_sftp
7. host: "localhost"
8. port: 22
9. read_username: "read"
10. read_password: "password"
11. write_username: "write"
12. write_password: "password"
13. path: /source22
14. -
15. name: test_two_sftp
16. host: "localhost"
17. port: 24
18. read_username: "read"
19. read_password: "password"
20. write_username: "write"
21. write_password: "password"
22. path: /source24
23. #server: http://localhost:8088
```

**custom存储**

使用自定义插件存储，具体配置为：

* type: 插件名称，为custom。custom是自定义存储插件类型，自定义存储插件[开发流程见官方文档](ide-ohpm-repo-storageplugin.md)。
* config: 插件配置，具体为：
  + export\_name：待书写插件export的类名。
  + plugin\_path：插件的绝对路径或者相对于ohpm-repo软件包的路径，建议将插件放在软件包的plugins目录下。
  + custom\_field：自定义字段，通过引入ohpm-repo解压包中libs/common/getStorageConfigInfo.js的getStorageConfigInfo方法获取自定义字段的值。
  + server: 本地仓库下载地址：
    - 当配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host不为0.0.0.0时，则**默认**取listen的完整格式，例如listen为127.0.0.1:8088，故server默认值为http://127.0.0.1:8088；
    - 如果配置项[listen](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_listen)的host为0.0.0.0，则server中的host默认为localhost，如http://localhost:8088。建议手动修改host为本机的ip/域名，例如listen为 0.0.0.0:8088，故server需配置为http://<本机ip/域名>:8088；
    - 如果需要通过反向代理来访问ohpm-repo服务，则该字段须配置为反向代理服务器的域名地址。多实例部署ohpm-repo时必须配置反向代理服务器，且需要配置[use\_reverse\_proxy](ide-ohpm-repo-configuration.md#section1074004784011)值为true。

参考配置如下：

```
1. store:
2. type: custom
3. config:
4. export_name: "MyStorage"
5. plugin_path: "plugins/storagePlugin/MyStorage.js"
6. custom_field: "test"
7. #server: http://localhost:8088
```

### use\_reverse\_proxy

* use\_reverse\_proxy: 是否使用反向代理选项。可选项：true/false， 默认：false。如果使用反向代理，必须配置为true，客户端IP地址将从请求头中的x-forwarded-for字段获取。

```
1. use_reverse_proxy: false
```

注意

当use\_reverse\_proxy配置为true时，必须在反向代理配置时刷新x-forwarded-for值（如果存在多级代理，只需要在最外层代理配置刷新），如果不刷新将存在x-forwarded-for数据被篡改风险，反向代理配置刷新x-forwarded-for命令如下：

```
1. proxy_set_header x-forwarded-for $remote_addr
```

### uplink

* uplink\_cache\_path：远程包缓存路径，默认路径为./uplink，支持相对和绝对路径配置，当配置为相对路径时，则以[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)为基准目录。
* uplink\_cache\_time：远程包metadata缓存时间，单位为小时，默认168小时，取值范围为(0, 8760]。

参考配置如下：

```
1. uplink_cache_path: ./uplink
2. uplink_cache_time: 168
```

### logs

* logs\_path: 日志存储，默认路径为./logs，支持相对路径和绝对路径配置，当配置为相对路径时，以[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_关于-deploy_root)为基准目录。

参考配置如下：

```
1. logs_path: ./logs
```

### loglevel

loglevel自定义配置，具体配置为：

* loglevel\_run：run日志文件的存储级别，默认级别为info，输出的日志信息级别高于设定的日志级别才会存储到run日志文件中。
* loglevel\_operate：operate日志文件的存储级别，默认级别为info，输出的日志信息级别高于设定的日志级别才会存储到operate日志文件中。
* loglevel\_access：access日志文件的存储级别，默认级别为info，输出的日志信息级别高于设定的日志级别才会存储到access日志文件中。

说明

* 日志级别由低到高分别是all、trace、debug、info、warn、error、fatal、mark 和 off。
* run、operate和access，日志级别不配置或者配置错误，默认为info。

参考配置如下：

```
1. loglevel_run: info
2. loglevel_operate: info
3. loglevel_access: info
```

### auth\_plugin

ohpm-repo从2.3.0版本开始支持自定义认证插件（需配套使用1.8.0及以上版本ohpm命令行工具），允许您开发定制化的认证插件来对接您自己的用户信息系统。自定义认证插件开发流程见[认证插件说明文档](ide-custom-auth-plugin.md)。

参数说明：

* name: 插件名称，自定义插件文件CustomAuth.js中定义的实现类名称，如果实现类为CustomAuth，故此处值为：CustomAuth 。
* path: 编译后插件文件CustomAuth.js的存储位置。支持绝对路径和相对路径，相对路径的基准为ohpm-repo解压根目录。

参考配置如下（默认不开启）：

```
1. #auth_plugin:
2. #  name: CustomAuth
3. #  path: plugins/CustomAuth.js
```

### field\_check\_plugin

ohpm-repo从5.1.3版本开始支持自定义元数据规则校验，可以对oh-package.json5中部分字段开发定制化的校验规则。自定义元数据规则校验插件开发流程见[自定义元数据规则校验插件说明文档](ide-custom-metadata-rule-validation-config.md)。

参数说明：

* config\_file\_path：字段校验配置文件路径，支持绝对路径和相对路径，相对路径的基准为ohpm-repo解压根目录，建议将文件存放在软件包的plugins/fieldCheckPlugin目录下，默认值为plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json。
* check\_func\_dir：字段校验函数文件所在目录路径，支持绝对路径和相对路径，相对路径的基准为ohpm-repo解压根目录，建议将目录设置为plugins/fieldCheckPlugin文件夹，默认值为plugins/fieldCheckPlugin。

参考配置如下（默认不开启）：

```
1. #field_check_plugin:
2. #  config_file_path:  plugins/fieldCheckPlugin/CustomExtensionValidationConfig.json
3. #  check_func_dir: plugins/fieldCheckPlugin
```

### content\_check\_plugin

ohpm-repo从5.2.0版本开始支持三方库字节码文件的OHMUrl版本一致性校验，可以对字节码har文件中module.abc文件中的OHMUrl的版本号与har文件中实际的版本号进行一致性校验，阻止不一致包的上传，以防止运行时崩溃。

注意

一致性检查将用到ark\_disasm工具及系统自带的tar解压工具。ark\_disasm工具位于命令行工具中，用于反编译module.abc文件，请先下载[命令行工具](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)，并将ark\_disasm工具所在路径（默认路径为command-line-tools/sdk/default/openharmony/toolchains）及tar解压工具的所在路径添加到系统环境变量中（对于Linux/macOS系统，请将bsdtar解压工具所在路径添加到系统环境变量中）。如在上传三方库过程中发现ark\_disasm导致报错，请联系管理员，确保您使用的DevEco Studio与ark\_disasm工具配套。

参数说明：

* name：固定为"OHMUrlCheck"

参考配置如下（默认不开启）：

```
1. #content_check_plugin:
2. #  name: 'OHMUrlCheck'
```

### compability\_log\_level

* compability\_log\_level: compatibleSdkVersion等兼容性字段检测日志等级，可选值：close、info、warn、error，默认为warn，参考配置如下：

```
1. compability_log_level: warn
```

### allow\_remove\_depended\_packages

* allow\_remove\_depended\_packages: 是否允许下架被其他组件依赖的包，可选项：true，false，默认为false，参考配置如下：

```
1. allow_remove_depended_packages: false
```

## 关于 deploy\_root

deploy\_root为ohpm-repo的部署目录，通过配置文件中字段<[deploy\_root](ide-ohpm-repo-configuration.md#zh-cn_topic_0000001745376470_deploy_root)>可进行配置。
