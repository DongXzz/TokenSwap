<h1 align="center">TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs</h1>

<p align="center"><a href="https://dongxzz.github.io/website/">Andong Hua</a><sup>1</sup>, Colton Bishop<sup>2</sup>, Igor Mordatch<sup>2</sup>, Arian Hosseini<sup>2</sup>, Jindong Gu<sup>2</sup>, Aleksandra Faust<sup>2</sup>, Rebecca Roelofs<sup>2</sup>, Yao Qin<sup>1,2</sup></p>

<p align="center"><sup>1</sup>University of California, Santa Barbara &nbsp;&nbsp; <sup>2</sup>Google DeepMind</p>

<p align="center"><b>NeurIPS 2026</b></p>

<p align="center">
  <a href="https://dongxzz.github.io/TokenSwap/"><img src="https://img.shields.io/badge/Project%20Page-363636?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTM1MiAyNTZjMCAyMi4yLTEuMiA0My42LTMuMyA2NEgxNjMuM2MtMi4yLTIwLjQtMy4zLTQxLjgtMy4zLTY0czEuMi00My42IDMuMy02NEgzNDguN2MyLjIgMjAuNCAzLjMgNDEuOCAzLjMgNjR6bTI4LjgtNjRINTAzLjljNS4zIDIwLjUgOC4xIDQxLjkgOC4xIDY0cy0yLjggNDMuNS04LjEgNjRIMzgwLjhjMi4xLTIwLjYgMy4yLTQyIDMuMi02NHMtMS4xLTQzLjQtMy4yLTY0em0xMTIuNi0zMkgzNzYuN2MtMTAtNjMuOS0yOS44LTExNy40LTU1LjMtMTUxLjZjNzguMyAyMC43IDE0MiA3Ny41IDE3MS45IDE1MS42em0tMTQ5LjEgMEgxNjcuN2M2LjEtMzYuNCAxNS41LTY4LjYgMjctOTQuN2MxMC41LTIzLjYgMjIuMi00MC43IDMzLjUtNTEuNUMyMzkuNCAzLjIgMjQ4LjcgMCAyNTYgMHMxNi42IDMuMiAyNy44IDEzLjhjMTEuMyAxMC44IDIzIDI3LjkgMzMuNSA1MS41YzExLjYgMjYgMjAuOSA1OC4yIDI3IDk0Ljd6bS0yMDkgMEgxOC42QzQ4LjYgODUuOSAxMTIuMiAyOS4xIDE5MC42IDguNEMxNjUuMSA0Mi42IDE0NS4zIDk2LjEgMTM1LjMgMTYwek04LjEgMTkySDEzMS4yYy0yLjEgMjAuNi0zLjIgNDItMy4yIDY0czEuMSA0My40IDMuMiA2NEg4LjFDMi44IDI5OS41IDAgMjc4LjEgMCAyNTZzMi44LTQzLjUgOC4xLTY0ek0xOTQuNyA0NDYuNmMtMTEuNi0yNi0yMC45LTU4LjItMjctOTQuNkgzNDQuM2MtNi4xIDM2LjQtMTUuNSA2OC42LTI3IDk0LjZjLTEwLjUgMjMuNi0yMi4yIDQwLjctMzMuNSA1MS41QzI3Mi42IDUwOC44IDI2My4zIDUxMiAyNTYgNTEycy0xNi42LTMuMi0yNy44LTEzLjhjLTExLjMtMTAuOC0yMy0yNy45LTMzLjUtNTEuNXpNMTM1LjMgMzUyYzEwIDYzLjkgMjkuOCAxMTcuNCA1NS4zIDE1MS42QzExMi4yIDQ4Mi45IDQ4LjYgNDI2LjEgMTguNiAzNTJIMTM1LjN6bTM1OC4xIDBjLTMwIDc0LjEtOTMuNiAxMzAuOS0xNzEuOSAxNTEuNmMyNS41LTM0LjIgNDUuMi04Ny43IDU1LjMtMTUxLjZINDkzLjR6Ii8%2BPC9zdmc%2B&logoColor=white" alt="Project Page"></a>
  <a href="https://arxiv.org/abs/2607.28640"><img src="https://img.shields.io/badge/Paper-363636?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTY0IDQ2NGw0OCAwIDAgNDgtNDggMGMtMzUuMyAwLTY0LTI4LjctNjQtNjRMMCA2NEMwIDI4LjcgMjguNyAwIDY0IDBMMjI5LjUgMGMxNyAwIDMzLjMgNi43IDQ1LjMgMTguN2w5MC41IDkwLjVjMTIgMTIgMTguNyAyOC4zIDE4LjcgNDUuM0wzODQgMzA0bC00OCAwIDAtMTQ0LTgwIDBjLTE3LjcgMC0zMi0xNC4zLTMyLTMybDAtODBMNjQgNDhjLTguOCAwLTE2IDcuMi0xNiAxNmwwIDM4NGMwIDguOCA3LjIgMTYgMTYgMTZ6TTE3NiAzNTJsMzIgMGMzMC45IDAgNTYgMjUuMSA1NiA1NnMtMjUuMSA1Ni01NiA1NmwtMTYgMCAwIDMyYzAgOC44LTcuMiAxNi0xNiAxNnMtMTYtNy4yLTE2LTE2bDAtNDggMC04MGMwLTguOCA3LjItMTYgMTYtMTZ6bTMyIDgwYzEzLjMgMCAyNC0xMC43IDI0LTI0cy0xMC43LTI0LTI0LTI0bC0xNiAwIDAgNDggMTYgMHptOTYtODBsMzIgMGMyNi41IDAgNDggMjEuNSA0OCA0OGwwIDY0YzAgMjYuNS0yMS41IDQ4LTQ4IDQ4bC0zMiAwYy04LjggMC0xNi03LjItMTYtMTZsMC0xMjhjMC04LjggNy4yLTE2IDE2LTE2em0zMiAxMjhjOC44IDAgMTYtNy4yIDE2LTE2bDAtNjRjMC04LjgtNy4yLTE2LTE2LTE2bC0xNiAwIDAgOTYgMTYgMHptODAtMTEyYzAtOC44IDcuMi0xNiAxNi0xNmw0OCAwYzguOCAwIDE2IDcuMiAxNiAxNnMtNy4yIDE2LTE2IDE2bC0zMiAwIDAgMzIgMzIgMGM4LjggMCAxNiA3LjIgMTYgMTZzLTcuMiAxNi0xNiAxNmwtMzIgMCAwIDQ4YzAgOC44LTcuMiAxNi0xNiAxNnMtMTYtNy4yLTE2LTE2bDAtNjQgMC02NHoiLz48L3N2Zz4%3D&logoColor=white" alt="Paper"></a>
  <a href="https://huggingface.co/datasets/dongx1997/TokenSwap-Bench"><img src="https://img.shields.io/badge/HuggingFace-363636?style=for-the-badge&logo=huggingface&logoColor=white" alt="HuggingFace"></a>
  <a href="#bibtex"><img src="https://img.shields.io/badge/BibTeX-363636?style=for-the-badge&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIj48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTQ0OCAyOTZjMCA2Ni4zLTUzLjcgMTIwLTEyMCAxMjBoLThjLTE3LjcgMC0zMi0xNC4zLTMyLTMyczE0LjMtMzIgMzItMzJoOGMzMC45IDAgNTYtMjUuMSA1Ni01NnYtOEgzMjBjLTM1LjMgMC02NC0yOC43LTY0LTY0VjE2MGMwLTM1LjMgMjguNy02NCA2NC02NGg2NGMzNS4zIDAgNjQgMjguNyA2NCA2NHYzMiAzMiA3MnptLTI1NiAwYzAgNjYuMy01My43IDEyMC0xMjAgMTIwSDY0Yy0xNy43IDAtMzItMTQuMy0zMi0zMnMxNC4zLTMyIDMyLTMyaDhjMzAuOSAwIDU2LTI1LjEgNTYtNTZ2LThINjRjLTM1LjMgMC02NC0yOC43LTY0LTY0VjE2MGMwLTM1LjMgMjguNy02NCA2NC02NGg2NGMzNS4zIDAgNjQgMjguNyA2NCA2NHYzMiAzMiA3MnoiLz48L3N2Zz4%3D&logoColor=white" alt="BibTeX"></a>
</p>

---

<p align="center"><img src="assets/tokenswap_example.png" width="90%"></p>

<p align="center"><img src="assets/fig1_overview.png" width="80%"></p>

Across **42 MLLMs**, we observe a pervasive modality gap, with performance decreasing by **4.2% to 47.4%** when moving from text-only to image-interleaved inputs.

---

## TokenSwap-Bench

TokenSwap operates at the **concept level**: it replaces individual textual concepts with semantically aligned natural images while preserving the surrounding context and structure. We apply TokenSwap to MMLU to construct TokenSwap-Bench, which contains **1,516 samples** with **6,946 image replacements**, averaging 4.58 replacements per sample.

| Task | Input |
|---|---|
| `tokenswap_text` | Text-only (original MMLU) |
| `tokenswap_img` | Image-interleaved |

**Modality gap** = Acc(`tokenswap_text`) − Acc(`tokenswap_img`)

The data is hosted on [Hugging Face](https://huggingface.co/datasets/dongx1997/TokenSwap-Bench) and downloaded automatically.

---

## Installation

We use [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) v0.7.3 (tested with PyTorch 2.7.0 and transformers 5.18.0).

```bash
pip install lmms_eval==0.7.3 qwen-vl-utils decord
git clone https://github.com/DongXzz/TokenSwap.git
```

## Evaluation

```bash
python -m lmms_eval \
    --model qwen3_vl \
    --model_args pretrained=Qwen/Qwen3-VL-8B-Instruct \
    --tasks tokenswap_text,tokenswap_img \
    --include_path TokenSwap/lmms_eval_tasks/tokenswap \
    --batch_size 1 --log_samples --output_path ./results/

python TokenSwap/scripts/compute_gap.py ./results/
```

Each image is inserted at its `<image N>` position in the prompt (images can also appear in the answer choices), so any lmms-eval chat model that accepts interleaved messages works out of the box.

---

## Reproducibility

The results in the paper were obtained with lmms-eval v0.3.1 and our own model wrappers. With lmms-eval v0.7.3, results may not be exactly reproduced. Below we compare the paper results with those obtained using lmms-eval v0.7.3 and the code in this repo (each cell: **paper / v0.7.3**). The two versions differ by less than 1 point in the modality gap.

| Model | Text | Image | Modality Gap | Δ Gap |
|:--|:--:|:--:|:--:|:--:|
| Qwen2.5-VL-3B | 67.0 / 66.3 | 45.8 / 45.2 | 21.2 / 21.1 | -0.1 |
| Qwen2.5-VL-7B | 67.7 / 66.0 | 52.9 / 50.9 | 14.8 / 15.0 | +0.2 |
| Qwen3-VL-4B | 70.7 / 70.6 | 52.3 / 52.0 | 18.4 / 18.6 | +0.2 |
| Qwen3-VL-8B | 78.2 / 79.4 | 57.1 / 57.5 | 21.1 / 22.0 | +0.9 |

---

## BibTeX

```bibtex
@inproceedings{hua2026tokenswap,
  title     = {TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs},
  author    = {Hua, Andong and Bishop, Colton and Mordatch, Igor and Hosseini, Arian and
               Gu, Jindong and Faust, Aleksandra and Roelofs, Rebecca and Qin, Yao},
  booktitle = {NeurIPS},
  year      = {2026}
}
```
