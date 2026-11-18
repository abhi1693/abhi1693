# Hi, I'm Abhimanyu Saharan

I build developer tools, web applications, and the infrastructure that runs them. My work spans Kubernetes and GitOps, Python and TypeScript, self-hosted systems, and AI agents with access to real tools.

I like working across the whole system: the application, its deployment, the automation around it, and what happens when something breaks. That shows up in both the products I build and the ARM64 Raspberry Pi homelab where I run and experiment with services.

I share implementations, debugging notes, and lessons from that work on [my blog](https://blog.abhimanyu-saharan.com). Recent writing covers homelab networking, Kubernetes, cluster cooling, and CI/CD.

## What I'm building

| Project | What it's for |
| --- | --- |
| [DevFeed](https://devfeed.tech) · [Code](https://github.com/abhi1693/devfeed.tech) | Developer news, tutorials, and releases in one reading feed, with public MCP access for discovering content through agents. |
| [Wardn AI](https://github.com/abhi1693/wardn-ai) | A control plane for AI agents and MCP tools: approved servers, scoped credentials, human approvals, execution, and audit trails. |
| [Wardn Hub](https://hub.wardnai.dev/) · [Code](https://github.com/abhi1693/wardn-hub) | A catalog for discovering and evaluating agent skills, with scanning and validation tooling. |
| [ShipyardHQ](https://shipyardhq.dev) · [Code](https://github.com/abhi1693/shipyardhq) | Product discovery beyond launch day, with directories, rankings, and launch analytics for apps, SaaS, AI tools, and APIs. |
| [GetEnvelope](https://github.com/abhi1693/getenvelope) | An early-stage project and service inbox with agent assistance; currently an application scaffold. |
| [Open-LLM Router](https://github.com/abhi1693/open-llm-router) | An OpenAI-compatible gateway for routing requests across model providers, with failover, logging, and metrics. |
| [NetBox SSOT](https://github.com/abhi1693/netbox-ssot) | Compare, review, and synchronize infrastructure data between NetBox instances. |
| [Firefly Importer](https://github.com/abhi1693/firefly-importer) | Bank, credit card, and mutual fund statement parsers and import workflows for Firefly III, with reconciliation checks. |

## Infrastructure and everyday automation

My [homelab](https://github.com/abhi1693/homelab) brings together ARM64 Raspberry Pis, Ansible, K3s, Rancher Fleet, custom container images, and development environments. It's where application work meets networking, storage, observability, backups, and recovery.

Alongside it, I maintain:

- [Shared GitHub Actions](https://github.com/abhi1693/actions) for reusable CI, container builds, scanning, and release automation.
- [Harbor ARM64 builds](https://github.com/abhi1693/harbor) to build and publish upstream Harbor components for ARM64.
- [Home Assistant configuration](https://github.com/abhi1693/home-assistant) with GitOps, family dashboards, custom integrations, and reproducible setup.
- [HA Sensors Gateway](https://github.com/abhi1693/ha-sensors-gateway) for narrowly scoped Home Assistant sensor and location webhooks.
- [qBittorrent Smart Queues](https://github.com/abhi1693/qbittorrent-smart-queues) for queue, quota, and health control.
- [Kubernetes Recommendation Engine](https://github.com/abhi1693/k8s-recommendation-engine) and [Music Assistant / YouTube Music tooling](https://github.com/abhi1693/music-assistant-yt-music).

## More projects

<details>
<summary>Experiments, libraries, earlier work, and supporting repositories</summary>

### Agents and workflow experiments

- [Jarvis](https://github.com/abhi1693/jarvis) — a local-first multimodal agent scaffold with persistent memory.
- [Agent Ops](https://github.com/abhi1693/agent-ops) — an application and workflow platform experiment.

### Libraries and integrations

- [Python Packer](https://github.com/abhi1693/python-packer) — a Python interface for Packer.
- [setup-browser](https://github.com/abhi1693/setup-browser) and [setup-megacmd](https://github.com/abhi1693/setup-megacmd) — GitHub Actions setup tools.
- [WPimporter](https://github.com/abhi1693/oc-wpimporter) — move WordPress posts into October CMS.

### Earlier PHP and Yii2 work

[User authentication](https://github.com/abhi1693/yii2-user) ·
[RBAC](https://github.com/abhi1693/yii2-rbac) ·
[System information](https://github.com/abhi1693/yii2-system-info) ·
[SMS](https://github.com/abhi1693/yii2-sms) ·
[Installer](https://github.com/abhi1693/yii2-installer) ·
[Enum helper](https://github.com/abhi1693/yii2-enum) ·
[Database configuration](https://github.com/abhi1693/yii2-config) ·
[Blog startup kit](https://github.com/abhi1693/yii2-app-blog-startup-kit) ·
[Advanced startup kit](https://github.com/abhi1693/yii2-app-advanced-startup-kit) ·
[Desk CMS](https://github.com/abhi1693/desk) ·
[Tux Tips user plugin](https://github.com/abhi1693/user) ·
[Tux Tips forum plugin](https://github.com/abhi1693/forum)

### Containers, configuration, and learning

[nginx-proxy](https://github.com/abhi1693/nginx-proxy) ·
[docker-barman](https://github.com/abhi1693/docker-barman) ·
[Docker demo](https://github.com/abhi1693/docker-demo-image) ·
[Dotfiles](https://github.com/abhi1693/dotfiles) ·
[Coder dotfiles](https://github.com/abhi1693/dotfiles-coder) ·
[Katacoda scenarios](https://github.com/abhi1693/katacoda-scenarios) ·
[GitHub Slideshow](https://github.com/abhi1693/github-slideshow)

### Sites and supporting repositories

[Personal blog](https://github.com/abhi1693/personal-blog) ·
[Blog discussions](https://github.com/abhi1693/personal-blog-discussions) ·
[Portfolio](https://github.com/abhi1693/portfolio) ·
[Wardn website](https://github.com/abhi1693/wardn-ai-website) ·
[This profile and its generator](https://github.com/abhi1693/abhi1693)

</details>

## On DevFeed

[![DevFeed card](https://devfeed.tech/api/v1/users/asaharan/card.svg)](https://devfeed.tech/users/asaharan)

## Reading from DevFeed 📖

A fresh reading list from [DevFeed](https://devfeed.tech): five recent articles on software, tools, and the systems behind them.

### 1. [CVE-2026-125275 - A device certificate whose CA isn't registered can keep a TLS handshake running forever](<https://cvefeed.io/vuln/detail/CVE-2026-125275>)

**Latest High/Critical Vulnerabilitiy Feed** · Article · Nov 17, 2026

In NervesHub versions 1.0.0 through before 2.5.4, an unauthenticated remote attacker can cause denial of service by presenting a TLS client certificate whose chain reaches a root trusted by the device endpoint but contains no CA registered in NervesHub.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-125275>)

---

### 2. [CVE-2026-107902 - FUJI ELECTRIC TELLUS Use-After-Free Vulnerability](<https://cvefeed.io/vuln/detail/CVE-2026-107902>)

**Latest High/Critical Vulnerabilitiy Feed** · News · Nov 17, 2026

FUJI ELECTRIC’s TELLUS and TELLUS Lite contain a use-after-free vulnerability. Opening a specially crafted V9 file may cause information exposure or arbitrary code execution on an affected product.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-107902>)

---

### 3. [IBM, RIKEN, and NVIDIA Improve Iron-Sulfur Cluster Quantum-Calculation Accuracy 79-Fold: The Key Was the Starting Point, Not the Quantum Circuit](<https://joho-todai.com/en/ibm-riken-nvidia-quantum-accuracy-iron-sulfur-cluster/>)

**Joho no Todai** · Article · Nov 17, 2026

Changing SQD’s classical reference state from restricted Hartree-Fock (RHF), which cannot represent the iron atoms’ opposing spins, to broken-symmetry unrestricted Hartree-Fock (BS-UHF) with a Noodleman initial guess improved the reference energy by about 534 mHa.

[Read article →](<https://joho-todai.com/en/ibm-riken-nvidia-quantum-accuracy-iron-sulfur-cluster/>)

---

### 4. [At SC26, Nvidia debuts new Rubin HPC chip, scientific research libraries](<https://siliconangle.com/2026/11/16/nvidia-debuts-new-rubin-hpc-chip-scientific-research-libraries/>)

**SiliconANGLE** · News · Nov 17, 2026

Nvidia announced a science-focused hardware and software lineup at SC26. Its planned Rubin HPC GPU, due in 2028, will have more than 50,000 CUDA cores, a new NVLink iteration, and sparse-data acceleration; the current Rubin GPU has over 28,000 CUDA cores.

[Read article →](<https://siliconangle.com/2026/11/16/nvidia-debuts-new-rubin-hpc-chip-scientific-research-libraries/>)

---

### 5. [AMD ROCm HRX's Loom 0.2 Expands C++ Support, Improved Targeting](<https://www.phoronix.com/news/HRX-Loom-0.2>)

**Phoronix** · Release · Nov 17, 2026

Loom 0.2 broadens complete-program C++ support and packaged AMD GPU/NPU and Vulkan execution, while expanding a shared target compiler across x86, AIE2P, AMDGPU, SPIR-V, and WebAssembly.

[Read article →](<https://www.phoronix.com/news/HRX-Loom-0.2>)


---

Updated 2026-11-18 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
