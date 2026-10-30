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

### 1. [The AI buildout's carbon bill could undo 15 years of power sector emissions cuts](<https://www.techspot.com/news/114385-ai-buildout-carbon-bill-could-undo-15-years.html>)

**TechSpot** · News · Oct 30, 2026

The Sierra Club estimates that planned US AI data centers could add 618 million metric tons of power-sector CO₂ emissions from 2025 to 2030, a 42% increase that would bring 2030 emissions to 2.1 billion metric tons and reverse 15 years of electricity-sector cuts.

[Read article →](<https://www.techspot.com/news/114385-ai-buildout-carbon-bill-could-undo-15-years.html>)

---

### 2. [Despite cloud boom, Amazon’s stock falls on disappointing earnings and revenue miss](<https://siliconangle.com/2026/10/29/despite-cloud-boom-amazons-stock-falls-disappointing-earnings-and-revenue-miss/>)

**SiliconANGLE** · News · Oct 30, 2026

Amazon shares fell more than 7% after third-quarter earnings per share ($1.89) and revenue ($201.94 billion) missed analyst estimates.

[Read article →](<https://siliconangle.com/2026/10/29/despite-cloud-boom-amazons-stock-falls-disappointing-earnings-and-revenue-miss/>)

---

### 3. [Report: Nvidia CEO Jensen Huang was targeted by a Chinese spy](<https://siliconangle.com/2026/10/29/report-nvidia-ceo-jensen-huang-was-targeted-by-a-chinese-spy/>)

**SiliconANGLE** · News · Oct 29, 2026

The New York Times reported that U.S. authorities suspected Megaspeed executive Alice Huang of gathering information for China through her relationship with Nvidia CEO Jensen Huang; Nvidia said their interactions were ordinary customer meetings and that he did not share sensitive trade secrets.

[Read article →](<https://siliconangle.com/2026/10/29/report-nvidia-ceo-jensen-huang-was-targeted-by-a-chinese-spy/>)

---

### 4. [OpenAI doubles ChatGPT Pro usage limits after backlash over planned 50% cut](<https://www.bleepingcomputer.com/news/artificial-intelligence/openai-doubles-chatgpt-pro-usage-limits-after-backlash-over-planned-50-percent-cut/>)

**BleepingComputer** · News · Oct 29, 2026

After customer feedback, OpenAI reversed a planned usage cut for existing $200 ChatGPT Pro subscribers and says limits will not be reduced for Pro plans priced at $100, $200, or $500, or Business Premium.

[Read article →](<https://www.bleepingcomputer.com/news/artificial-intelligence/openai-doubles-chatgpt-pro-usage-limits-after-backlash-over-planned-50-percent-cut/>)

---

### 5. [API credits benefit for eligible ChatGPT subscriptions](<https://simonwillison.net/2026/Oct/29/api-credits/>)

**Simon Willison's Weblog** · News · Oct 29, 2026

OpenAI’s stated benefit gives subscribers on $100, $200, or $500 monthly plans an equal amount in API credits to apply to one of their API organizations. The excerpt says this closely matches Anthropic’s earlier offer for its Max and Team subscribers, whose credits expire.

[Read article →](<https://simonwillison.net/2026/Oct/29/api-credits/>)


---

Updated 2026-10-30 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
