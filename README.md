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

### 1. [Check a subagent's OpenShell policy against a boundary](<https://nirmata.com/2026/11/12/openshell-policy-ceilings-and-least-privilege-delegation/>)

**Nirmata** · Tutorial

OpenShell’s Policy Prover checks offline whether a candidate policy stays within a maximum-access boundary; only &#96;within&#95;boundary&#96; passes, and the check does not apply or enforce the policy.

[Read article →](<https://nirmata.com/2026/11/12/openshell-policy-ceilings-and-least-privilege-delegation/>)

---

### 2. [A decade in, KubeVirt pushes virtual machines into the AI agent era](<https://siliconangle.com/2026/11/11/confidential-computing-ai-agents-push-kubevirt-vms-forward-kubeconna/>)

**SiliconANGLE** · News · Nov 12, 2026

KubeVirt, which runs virtual machines alongside containers on Kubernetes, has graduated from the Cloud Native Computing Foundation and is being positioned for AI workload isolation. Its maintainers describe VMs as providing larger isolation and heavy compute, with pods offering scaling for cache applications.

[Read article →](<https://siliconangle.com/2026/11/11/confidential-computing-ai-agents-push-kubevirt-vms-forward-kubeconna/>)

---

### 3. [Announcing the Relate by Neo4j Hackathon 2026: Build AI Agents on an Embedded Graph Database](<https://neo4j.com/blog/graph-database/announcing-the-relate-by-neo4j-hackathon-2026-build-ai-agents-on-an-embedded-graph-database/>)

**Neo4j** · News · Nov 12, 2026

Relate by Neo4j is an open-source embedded graph database for AI agents, offered as a library inside an application without a server or signup. Graphs can be kept in memory, a directory, or a single file; local relationship and vector lookups avoid network calls.

[Read article →](<https://neo4j.com/blog/graph-database/announcing-the-relate-by-neo4j-hackathon-2026-build-ai-agents-on-an-embedded-graph-database/>)

---

### 4. [Nvidia’s board reportedly preparing to oust CEO Jensen Huang after reports of a second affair](<https://siliconangle.com/2026/11/11/nvidias-board-reportedly-preparing-to-oust-jensen-huang-after-reports-of-a-second-affair/>)

**SiliconANGLE** · News · Nov 12, 2026

Reports in the New York Times and Wall Street Journal describe two separate issues facing Nvidia CEO Jensen Huang: an alleged relationship with Healthcare Vice President Kimberly Powell, and his reported admission of an affair with Alice Huang, a former data-center supplier CEO suspected of…

[Read article →](<https://siliconangle.com/2026/11/11/nvidias-board-reportedly-preparing-to-oust-jensen-huang-after-reports-of-a-second-affair/>)

---

### 5. [Google enters decision model market with Gemini Decisions API](<https://siliconangle.com/2026/11/11/google-enters-the-decision-model-market-with-gemini-decisions-api/>)

**SiliconANGLE** · Release · Nov 12, 2026

Gemini Decision 1 is a decision model for yes/no, multiple-choice, and rating questions, returning concise answers with confidence scores. Google says it costs nearly five times less than Gemini 3.5 Flash-Lite; the API charges $0.10 per million input tokens and no output-token fees.

[Read article →](<https://siliconangle.com/2026/11/11/google-enters-the-decision-model-market-with-gemini-decisions-api/>)


---

Updated 2026-11-13 UTC · Refreshed daily through [DevFeed's public MCP](https://devfeed.tech/mcp).
