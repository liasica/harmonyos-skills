---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparing-input-data-and-benchmark
title: 输入数据和标杆数据准备
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 数据准备和配置说明 > 输入数据和标杆数据准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:429522b1ab3d73a242010a25c79b10826d8c70ab4c2c0d609df6609d86cc13c0
---

使用AscendC调测工具进行算子调测前，必须提供算子的[输入数据和标杆数据](cannkit-commissioning-tools.md)。

* 输入数据（input数据）：固定shape算子运行时的输入数据，bin格式。
* 标杆数据（golden数据）：根据输入数据计算出来的真值数据，用于与输出数据进行精度比对，bin格式。

本章节提供多种方式来准备数据，开发者可以根据实际情况选择合适的方式。

* **方式1：采用外部提供的input/golden数据。**

  开发者采用外部数据源进行算子调测，一般适合首次调测场景。

  在算子信息json配置文件中，将gen\_data配置为false，data\_file配置为输入数据、标杆数据对应的路径（必须为绝对路径），示例如下。

  ```
  1. {
  2. "gen_data": false,
  3. "inputs": [
  4. {
  5. "data_file": "/path/to/input_data_q.bin"
  6. }
  7. ],
  8. "outputs": [
  9. {
  10. "data_file": "/path/to/golden_data_out.bin"
  11. }
  12. ]
  13. }
  ```

  若外部提供的数据是.pt文件，需要转换为.bin文件，以PyTorch为例：

  ```
  1. import torch
  2. model = torch.load('model.pt')   # 加载.pt文件
  3. torch.save(model, 'model.bin')   # 将模型参数保存为二进制文件
  ```
* **方式2：采用已生成过的input/golden数据，无需重新生成。**

  当开发者需要多次重跑，建议直接使用历史生成的数据，避免重复生成，导致调测耗时过长。

  在算子信息json配置文件中，将gen\_data配置为false，data\_file配置为输入数据、标杆数据对应的bin文件名（不含路径信息，默认在当前路径下查找数据文件），示例如下。

  ```
  1. {
  2. "gen_data": false,
  3. "inputs": [
  4. {
  5. "data_file": "input_data_q.bin"
  6. }
  7. ],
  8. "outputs": [
  9. {
  10. "data_file": "golden_data_out.bin"
  11. }
  12. ]
  13. }
  ```
* **方式3：采用工具随机生成input数据。**

  开发者未准备任何数据，可采用工具随机生成的input数据，生成的bin数据文件默认在当前路径下的对应算子的data文件夹中。该场景下没有golden数据，因此不支持精度比对。

  在算子信息json配置文件中，将gen\_data配置为true，data\_script配置为空字符串或null，data\_file配置为输入数据、标杆数据对应的bin文件名（不含路径信息，默认在当前路径下查找数据文件），示例如下。

  ```
  1. "data_script": "",
  2. "gen_data": true,

  4. "shape": [1, 16384],
  5. "data_file": "sample.bin",
  ```
* **方式4：采用脚本生成input/golden数据。**

  开发者自行准备数据生成脚本（一般是.py文件），同时配置算子信息json配置文件。

  将gen\_data配置为true，data\_script配为数据生成脚本路径（以FlashAttentionScore算子为例），data\_file配置为输入数据、标杆数据对应的bin文件名（不含路径信息，默认在当前路径下查找数据文件），示例如下。

  ```
  1. "data_script": "${fa_case_dir}/flash_attention_score_golden.py",
  2. "gen_data": true,

  4. "data_file": "sample.bin",
  ```

  生成数据时，会调用该脚本，并固定传入以下参数：

  sys.argv[1]：输入的算子json配置文件。

  sys.argv[2]：输出bin文件路径（工作路径下的data文件夹，例如debug\_workspace/FlashAttentionScore/data/）。

  + 开发者需要根据输入的sys.argv[1]读取算子json配置文件内容，获取生成数据所需的算子shape信息、数据文件的文件名，并在脚本中适配生成的文件名。
  + 开发者需要根据输入的sys.argv[2]设置存放input/output数据文件的路径，将生成的文件保存到该路径下。
