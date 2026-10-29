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

### 1. [Smaller apps and faster GPU inference with LiteRT in Google Play services](<https://developers.googleblog.com/smaller-apps-and-faster-gpu-inference-with-litert-in-google-play-services/>)

**Google Developers Blog** · Release

LiteRT in Google Play services adds GPU inference through the CompiledModel API, which the source says ran about 1.4× faster than the legacy GPU delegate in its testing.

[Read article →](<https://developers.googleblog.com/smaller-apps-and-faster-gpu-inference-with-litert-in-google-play-services/>)

---

### 2. [Hill-Climbing Agent Quality with Agents CLI Evaluation](<https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/>)

**Google Developers Blog** · Tutorial

Agents CLI supports an evaluation loop that runs agent cases, grades traces, compares results per case, and analyzes failures; ADK projects can also use eval optimize to propose prompt variants.

[Read article →](<https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/>)

---

### 3. [Energy-efficient inference chip developer FuriosaAI raises $620M to solve the data center power bottleneck](<https://siliconangle.com/2026/10/28/energy-efficient-inference-chip-developer-furiosaai-raises-620m-to-solve-the-data-center-power-bottleneck/>)

**SiliconANGLE** · News · Oct 29, 2026

FuriosaAI raised $620 million at a reported $2.9 billion valuation to scale production of its energy-efficient inference chips.

[Read article →](<https://siliconangle.com/2026/10/28/energy-efficient-inference-chip-developer-furiosaai-raises-620m-to-solve-the-data-center-power-bottleneck/>)

---

### 4. [Microsoft’s stock rises on solid earnings and revenue beat, with Azure growing 48%](<https://siliconangle.com/2026/10/28/microsofts-stock-rises-on-solid-earnings-and-revenue-beat-with-azure-growing-48/>)

**SiliconANGLE** · News · Oct 29, 2026

Microsoft beat fiscal 2027 first-quarter expectations, with revenue up 19% to $92.28 billion and net income rising to $36.63 billion. Azure revenue grew more than 48% to $33.17 billion, above forecasts, despite delays from some third-party providers.

[Read article →](<https://siliconangle.com/2026/10/28/microsofts-stock-rises-on-solid-earnings-and-revenue-beat-with-azure-growing-48/>)

---

### 5. [Visual Studio Code 1.145 (Insiders)](<https://code.visualstudio.com/updates/v1_145>)

**Visual Studio Code** · Release

VS Code 1.145 Insiders adds Agents window improvements and experimental workflow options. Bulk worktree cleanup now shows progress, keeps completed results visible, and allows failed cleanups to be retried; cleanup size estimates can appear sooner for unchanged idle sessions.

[Read article →](<https://code.visualstudio.com/updates/v1_145>)


---

Updated 2026-10-29 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
