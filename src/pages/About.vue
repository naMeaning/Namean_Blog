<template>
  <section class="section about">
    <h2 class="section-title">关于我们</h2>
    <p>
      Namean Studio 专注于科技行业的品牌与内容体验，通过结构化信息设计、产品叙事与视觉系统，帮助客户建立可信赖的市场沟通方式。
    </p>
    <div class="about-grid">
      <div class="card">
        <h3>服务客户</h3>
        <p>科技企业、SaaS 平台、创新团队与行业媒体。</p>
      </div>
      <div class="card">
        <h3>擅长领域</h3>
        <p>品牌官网、产品体验升级、内容体系搭建。</p>
      </div>
      <div class="card">
        <h3>合作方式</h3>
        <p>咨询 + 执行一体化交付，按项目或长期服务。</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about {
  max-width: 960px;
}

.about-grid {
  margin-top: 24px;
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.about p {
  color: #b2b9c7;
  line-height: 1.7;
}
</style>
