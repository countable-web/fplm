<template>
  <div>
    <p class="text-center p-3">
      {{ error }}
      <br />
      {{ content }}
      <a :href="'mailto:' + email + '?subject=' + subject">{{ email }}</a>
    </p>
  </div>
</template>

<script>
export default {
  props: {
    email: {
      type: String,
      default: 'info@fpcc.ca'
    },
    subject: {
      type: String,
      default: ''
    },
    content: {
      type: String,
      default: "Didn't find what you were looking for? Email us at"
    },
    error: {
      type: String,
      default: ''
    }
  }
}
</script>
<style></style>
