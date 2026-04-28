---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-incremental-build
title: 增量构建
breadcrumb: 指南 > 构建应用 > 提升构建效率 > 增量构建
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0aabe8acf5b003d2686a7a284ed53d088a11c0617f6aeee37c7fe98eb561ea72
---

增量构建是Hvigor执行任务的一种优化，如果在两次执行任务过程中，执行任务的输入和输出没有更改，Hvigor会跳过该任务的执行。

Hvigor自定义任务要与增量构建兼容，需指定输入和输出，有关增量构建的更多介绍，请查看[原理介绍](ide-hvigor-incremental-build.md#section18840102817255)。

Hvigor默认启用增量构建，您也可以通过以下几种方式来控制是否启用增量构建：

* 通过DevEco Studio菜单栏构建：
  + 点击**File >** **Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Build, Execution, Deployment > Build Tools > Hvigor**，勾选或取消勾选字段**Re-execute the task in incremental mode**。
* 通过命令行构建：
  + 执行命令，其中<task>替换为具体任务名：

    ```
    1. // 启用增量构建
    2. hvigorw <task> --incremental
    3. // 关闭增量构建
    4. hvigorw <task> --no-incremental
    ```
  + 在[hvigor-config.json5](ide-hvigor-set-options.md)中配置execution.incremental选项。

## 原理介绍

任何构建工具的一个重要部分是能够避免重复执行已经执行完成的工作。在重复编译时，如果之前的源文件已经被编译过，除非发生了影响输入输出的更改，那么该文件就不需要重新编译。编译过程本身会耗费大量时间，因此跳过此种任务的编译，将会节省大量时间。

Hvigor自然支持此种增量构建行为。当您执行任务且控制台输出任务被标记为UP-TO-DATE，这意味着增量构建正在工作。

在DevEco Studio中，第一次构建后会生成build缓存目录，再次构建时，

* 如果执行**Build > Clean Project**操作后，再重新build，则会执行全量构建；
* 如果没有执行**Build > Clean Project**操作，则重新build时会执行增量构建。

### 任务的输入和输出

在正常情况下，任务根据一些输入生成一些输出。作为增量构建的一部分，Hvigor记录上次构建的任何任务的输入和输出情况，对比当次构建的输入和输出，如果没有发生更改，那么Hvigor将认为该任务没有更改，从而跳过该任务的执行。因此也请注意，尽管任务在通常情况下至少有一个输入，但是在定义任务时，请至少定义一个输出，否则增量构建将无法工作。

对此定义增量任务，您只需告诉Hvigor哪些任务属性是输入，哪些任务属性是输出。如果任务属性影响了输出，请务必将其注册为输入，否则任务将可能被视为最新，与预期效果不一致。相反，如果任务属性不影响输出，请不要将其注册为输入，否则任务将可能会在不需要时被执行。同时请注意非确定性任务不应配置为增量任务，因为这些任务可能为完全相同的输入生成不同的输出，导致最新检查不起作用。

### 它是如何工作的

在第一次执行之前，Hvigor会获取输入的快照信息，该信息包括输入文件名称、路径、大小、最后修改时间以及对应的哈希值。任务执行成功之后，Hvigor会获取输出的快照信息，该信息包括输出文件名称、路径、大小、最后修改时间以及对应的哈希值。当然，Hvigor对任务本身也进行了快照存储。Hvigor会在下次执行任务时会保留这两个快照信息。

此后每次执行任务之前，Hvigor都会获取输入和输出的新快照信息。如果新快照信息与之前的快照信息相同，Hvigor就会认为输出已经是最新的并且跳过该任务的执行。如果它们不相同，Hvigor就会执行该任务，执行成功之后，输入和输出的新快照信息将被存储。
