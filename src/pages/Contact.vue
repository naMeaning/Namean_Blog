<template>
  <section class="section contact">
    <h2 class="section-title">联系与合作</h2>
    <p>如果你希望开展品牌或产品合作，可以通过以下方式联系我。</p>
    <div class="contact-card">
      <div>
        <h3>联系方式</h3>
        <p>邮箱：hello@namean.studio</p>
        <p>微信：Namean-Design</p>
      </div>
      <div>
        <h3>合作方向</h3>
        <ul>
          <li>官网与品牌叙事</li>
          <li>产品体验与增长</li>
          <li>内容策略与行业白皮书</li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
.contact {
  max-width: 900px;
}

.contact p {
  color: #b2b9c7;
  margin-bottom: 16px;
}

.contact-card {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}

.contact-card ul {
  list-style: none;
  display: grid;
  gap: 8px;
  color: #b2b9c7;
}
</style>
