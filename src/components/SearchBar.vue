<template>
  <div class="search-bar">
    <span>🔍</span>
    <input v-model="modelValue" type="text" placeholder="搜索文章 / 项目" />
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  modelValue: {
    type: String,
    default: ""
  }
});

const emit = defineEmits(["update:modelValue"]);

const modelValue = computed({
  get: () => props.modelValue,
  set: (value) => emit("update:modelValue", value)
});
</script>
