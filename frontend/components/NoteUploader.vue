<template>
  <div>
    <label for="text-title" class="font-08 color-dark-gray font-weight-bold"
      >Title</label
    >
    <b-form-input
      id="text-title"
      v-model="title"
      placeholder="Enter a title for this note/text"
      aria-describedby="text-title-help text-title-feedback"
      size="sm"
      class=""
      :state="titlestate"
    ></b-form-input>

    <b-form-invalid-feedback id="text-title-feedback">
      Title is required
    </b-form-invalid-feedback>

    <label for="text-area" class="font-08 color-dark-gray font-weight-bold mt-2"
      >Text/Note</label
    >
    <b-form-textarea
      id="text-area"
      v-model="text"
      size="sm"
      placeholder="Add your note/text"
      aria-describedby="text-area-help text-area-feedback"
      :state="textstate"
    ></b-form-textarea>

    <b-form-invalid-feedback id="text-area-feedback">
      This is required
    </b-form-invalid-feedback>

    <CommunityOnly class="mt-3" :commonly.sync="commonly"></CommunityOnly>

    <b-button size="sm" variant="dark" class="mt-2" @click="handleNoteUpload"
      >Upload</b-button
    >
  </div>
</template>
<script>
import { getFormData } from '@/plugins/utils.js'
import CommunityOnly from '@/components/CommunityOnly.vue'
export default {
  components: {
    CommunityOnly
  },
  props: {
    id: {
      default: null,
      type: Number
    },
    type: {
      default: 'placename',
      type: String
    }
  },
  data() {
    return {
      title: null,
      text: null,
      titlestate: null,
      textstate: null,
      commonly: null
    }
  },
  methods: {
    resetState() {
      this.title = null
      this.text = null
      this.titlestate = null
      this.textstate = null
    },
    async handleNoteUpload(e) {
      if (!this.title) {
        this.titlestate = false
      }

      if (!this.text) {
        this.textstate = false
      }

      if (!this.title || !this.text) {
        return false
      }

      const formData = getFormData(
        {
          name: this.title,
          description: this.text,
          file_type: 'text',
          type: this.type,
          id: this.id,
          community_only: this.commonly === 'accepted'
        },
        true
      )

      try {
        const result = await this.uploadNote(formData)
        if (
          result.request.status === 201 &&
          result.request.statusText === 'Created'
        ) {
          this.$root.$emit('fileUploaded', result.data)
        } else {
          throw result
        }
      } catch (e) {
        console.error(e)
        this.$root.$emit('notification', {
          title: 'Failed',
          message: 'Note/Text Upload Failed, please try again',
          time: 1500,
          variant: 'danger'
        })
      }
      this.resetState()
    },

    async uploadNote(formData) {
      const result = await this.$store.dispatch('file/uploadMedia', formData)
      return result
    }
  }
}
</script>
<style></style>
