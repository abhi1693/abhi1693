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

### 1. [ACEMAGIC Kron Mini K5 Review – Part 3: Ubuntu 26.04 on an entry-level Wildcat Lake mini PC](<https://www.cnx-software.com/2026/11/05/acemagic-kron-mini-k5-review-part-3-ubuntu-26-04-on-an-entry-level-wildcat-lake-mini-pc/>)

**CNX Software – Embedded Systems News** · Article · Nov 05, 2026

The ACEMAGIC Kron Mini K5 runs Ubuntu 26.04.1 alongside Windows 11 after the reviewers disabled Secure Boot to resolve an installation error.

[Read article →](<https://www.cnx-software.com/2026/11/05/acemagic-kron-mini-k5-review-part-3-ubuntu-26-04-on-an-entry-level-wildcat-lake-mini-pc/>)

---

### 2. [What Makes a Quantum Company Valuable?](<https://www.eetimes.com/what-makes-a-quantum-company-valuable/>)

**EE Times** · News · Nov 05, 2026

Quantum companies need a credible path from technical progress to customer value, investors say. Qubits Ventures’ Nardo Manaloto looks for intermediate products that solve real problems and can earn revenue while advancing the long-term roadmap.

[Read article →](<https://www.eetimes.com/what-makes-a-quantum-company-valuable/>)

---

### 3. [CVE-2026-123033 - TrueNAS SCALE middlewared Authentication Bypass](<https://cvefeed.io/vuln/detail/CVE-2026-123033>)

**Latest High/Critical Vulnerabilitiy Feed** · Article · Nov 05, 2026

Before TrueNAS SCALE 25.10.8 (or the corresponding fixes in other release trains), middlewared’s HA peer-authentication hook could grant unauthenticated full-administrator API access, including root command execution, to a connection from the same layer-2 network segment.

[Read article →](<https://cvefeed.io/vuln/detail/CVE-2026-123033>)

---

### 4. [Google AI Research Releases Agile Deliberation Framework for Gray-Area Image Classifiers](<https://www.marktechpost.com/2026/11/04/google-agile-deliberation-subjective-image-classifiers/>)

**MarkTechPost** · Article · Nov 05, 2026

Agile Deliberation helps users define subjective image categories by reviewing borderline examples and turning disagreements into revised classifier definitions. It first breaks a concept into up to three units with candidate positive and negative subconcepts.

[Read article →](<https://www.marktechpost.com/2026/11/04/google-agile-deliberation-subjective-image-classifiers/>)

---

### 5. [Companies are spending more on AI governance and getting less control](<https://www.helpnetsecurity.com/2026/11/05/dnsfilter-shadow-ai-cost-report/>)

**Help Net Security** · News · Nov 05, 2026

The excerpt reports a gap between AI governance spending and practical oversight. In DNSFilter’s survey, 40.3% named AI security and governance as the next priority for added security spending, yet 61.5% could not confirm all security tools were properly configured and 61.8% could not confirm…

[Read article →](<https://www.helpnetsecurity.com/2026/11/05/dnsfilter-shadow-ai-cost-report/>)


---

Updated 2026-11-06 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
