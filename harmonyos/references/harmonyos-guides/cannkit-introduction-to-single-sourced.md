---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-introduction-to-single-sourced
title: 同源算子调测样例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > 调测工具样例与参数说明 > 同源算子调测样例
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:01a9f724afd816d5c78d63228fd161cd17262907142b4924dcaaeed08b5d9b72
---

同源算子指算子的输入和输出为同一地址，算子在计算完成后，把原有的输出结果直接覆盖在输入的地址上，同源算子调测时，需要在outputs中配置对应的算子输出，输出名称类型要和input保持一致。

## 同源算子配置示例

tensor类：定义的json数据的object中name shape dtype format在inputs和outputs里必须一致，但是data\_file必须可区分，在调测过程中，这两个文件会同步到data的目录下，如果文件名相同，则会导致JSON文件被覆盖。

```
1. {
2. "op_type": "AbsCustom",
3. "data_script": "./add_golden.py",
4. "checkpoint_dump_path": "./debug_workspace/AddCustom/data/dump",
5. "gen_data": true,
6. "inputs": [
7. {
8. "name": "x",
9. "dtype": "float16",
10. "format": "ND",
11. "ignore": false,
12. "shape": [32],
13. "param_type": "required",
14. "data_file": "x.bin"
15. }

17. ],
18. "outputs": [
19. {
20. "name": "x",
21. "dtype": "float16",
22. "format": "ND",
23. "ignore": false,
24. "shape": [32],
25. "param_type": "required",
26. "data_file": "ref_x.bin"
27. }
28. ]

30. }
```

tensorlist类：list中的每个对象必须是同源且数量位置一致。

```
1. {
2. "op_type": "ForeachACosInplace",
3. "data_script":"ForeachACosInplace.py",
4. "gen_data": true,
5. "inputs": [
6. [{
7. "name": "inputs",
8. "dtype": "float32",
9. "format": "ND",
10. "param_type": "required",
11. "shape": [
12. 10
13. ],
14. "data_file": "x0.bin"
15. },{
16. "name": "inputs1",
17. "dtype": "float32",
18. "format": "ND",
19. "param_type": "required",
20. "shape": [
21. 8,8
22. ],
23. "data_file": "x1.bin"
24. }]
25. ],
26. "outputs": [
27. [{
28. "name": "inputs",
29. "dtype": "float32",
30. "format": "ND",
31. "param_type": "required",
32. "shape": [
33. 10
34. ],
35. "data_file": "ref_x0.bin"
36. },{
37. "name": "inputs1",
38. "dtype": "float32",
39. "format": "ND",
40. "param_type": "required",
41. "shape": [
42. 8,8
43. ],
44. "data_file": "ref_x1.bin"
45. }
46. ]
47. ]
48. }
```
