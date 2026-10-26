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

### 1. [Redox OS Landed Nice Performance Improvements In September](<https://www.phoronix.com/news/Redox-OS-September-2026>)

**Phoronix** · News · Oct 26, 2026

Redox OS’s September 2026 update reports performance gains from several kernel changes. Direct context switching bypasses the scheduler for system service calls, avoiding an expensive BTreeMap path; the excerpt reports 24% lower IPC latency and about 5% better I/O performance with small buffers.

[Read article →](<https://www.phoronix.com/news/Redox-OS-September-2026>)

---

### 2. [OpenSSL 4.1.0: What’s new, what’s removed, and what’s still broken](<https://www.helpnetsecurity.com/2026/10/26/openssl-4-1-0-released/>)

**Help Net Security** · Release · Oct 25, 2026

OpenSSL 4.1.0 adds DTLS 1.3 but ships with four known DTLS bugs. Listener errors can be misreported as SSL&#95;ERROR&#95;WANT&#95;READ, and retryable writes as SSL&#95;ERROR&#95;SYSCALL; a server handshake may abort after packet loss, and KeyUpdate can discard a lost NewSessionTicket instead of retransmitting it.

[Read article →](<https://www.helpnetsecurity.com/2026/10/26/openssl-4-1-0-released/>)

---

### 3. [Hackaday Links: October 25, 2026](<https://hackaday.com/2026/10/25/hackaday-links-october-25-2026/>)

**Hackaday** · News · Oct 25, 2026

Denmark’s trial of Collabora reportedly ran into collaboration problems when its users exchanged documents with peers using Microsoft Office, and was quietly abandoned.

[Read article →](<https://hackaday.com/2026/10/25/hackaday-links-october-25-2026/>)

---

### 4. [Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding Model](<https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/>)

**MarkTechPost** · Release · Oct 25, 2026

Nanbeige4.3-33B is a 33B dense Apache 2.0 model for agentic coding and office tasks, with a 524,288-token context; the lab also released a Base version for custom post-training.

[Read article →](<https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/>)

---

### 5. [Silicon Photonic Modulator Reaches 200 Gb/s PAM4 With Reduced DSP (Science Tokyo, Yokohama, AIST, PETRA)](<https://semiengineering.com/silicon-photonic-modulator-reaches-200-gb-s-pam4-with-reduced-dsp-science-tokyo-yokohama-aist-petra/>)

**Semiconductor Engineering** · News · Oct 25, 2026

Researchers from Institute of Science Tokyo, Yokohama National University, AIST, and PETRA report a silicon photonic crystal waveguide slow-light modulator with a built-in electro-optic equalizer. The paper title identifies a 200G/λ low-voltage design intended to reduce digital signal processing.

[Read article →](<https://semiengineering.com/silicon-photonic-modulator-reaches-200-gb-s-pam4-with-reduced-dsp-science-tokyo-yokohama-aist-petra/>)


---

Updated 2026-10-26 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
