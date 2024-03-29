<template>
  <div>
    <div>
      <b-alert
        v-if="media.status === 'UN'"
        variant="warning"
        show
        class="d-inline-block p-1 font-08"
        >Unverified Media</b-alert
      >
      <b-alert
        v-else-if="media.status === 'VE'"
        variant="primary"
        show
        class="d-inline-block p-1 font-08"
      >
        Verified Media</b-alert
      >
      <b-alert
        v-else-if="media.status === 'FL'"
        variant="danger"
        show
        class="d-inline-block p-1 font-08"
        >Flagged Media</b-alert
      >
      <b-alert
        v-else-if="media.status === 'RE'"
        variant="danger"
        show
        class="d-inline-block p-1 font-08"
        >Rejected Media</b-alert
      >
      <b-alert
        v-if="communityOnly"
        variant="success"
        show
        class="d-inline-block p-1 font-08"
        >Community Only</b-alert
      >
      <div v-if="this.delete" class="float-right">
        <DeleteMedia :id="media.id" :media="media"></DeleteMedia>
      </div>
    </div>
    <div v-if="media.name" class="font-08 color-gray">
      <span>Name: </span>
      <span class="word-break-all">{{ media.name }}</span>
      <span v-if="flag" class="float-right cursor-pointer">
        <FlagModal
          :id="media.id"
          title="Report"
          style="font-size: 1rem;"
          :media="media"
        ></FlagModal>
      </span>
    </div>
    <div v-if="media.description" class="font-08 color-gray">
      <span>Description: </span>
      <span class="word-break-all">{{ media.description }}</span>
    </div>
    <div
      v-if="getGenericFileType(media.file_type) === 'image'"
      class="d-flex justify-content-center"
    >
      <img
        class="media-image cursor-pointer"
        :src="getMediaUrl(media.media_file, server)"
        :alt="media.name"
        @click="handleImageClick($event, media)"
      />
    </div>

    <div v-if="getGenericFileType(media.file_type) === 'audio'">
      <audio controls class="uploaded-audio">
        <source
          :src="getMediaUrl(media.media_file, server)"
          :type="media.file_type"
        />
        <p>
          Your browser doesn't support HTML5 audio. Here is a
          <a :href="getMediaUrl(media.media_file, server)">link to the audio</a>
          instead.
        </p>
      </audio>
    </div>

    <div
      v-if="getGenericFileType(media.file_type) === 'youtube'"
      class="word-break-all d-flex justify-content-center"
    >
      <iframe
        width="100%"
        :src="`https://www.youtube.com/embed/${getYoutubeId(media.url)[2]}`"
        frameborder="0"
        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>

    <div
      v-if="getGenericFileType(media.file_type) === 'vimeo'"
      class="word-break-all d-flex justify-content-center"
    >
      <iframe
        v-if="vimeo.id"
        :src="`https://player.vimeo.com/video/${vimeo.id}`"
        width="100%"
        frameborder="0"
        allow="autoplay; fullscreen"
        allowfullscreen
      ></iframe>
    </div>

    <div
      v-if="getGenericFileType(media.file_type) === 'other'"
      class="word-break-all d-flex justify-content-center"
    >
      <b-button
        variant="dark"
        size="sm"
        class="mt-2"
        :href="getMediaUrl(media.file_type, server)"
        >Download</b-button
      >
    </div>

    <div
      v-if="getGenericFileType(media.file_type) === 'note'"
      class="word-break-all d-flex justify-content-center"
    ></div>
  </div>
</template>
<script>
import FlagModal from '@/components/Flag/FlagModal.vue'
import DeleteMedia from '@/components/DeleteMedia.vue'
import {
  getGenericFileType,
  getMediaUrl,
  getYoutubeId
} from '@/plugins/utils.js'
export default {
  components: {
    FlagModal,
    DeleteMedia
  },
  props: {
    media: {
      default: null,
      type: Object
    },
    flag: {
      default: true,
      type: Boolean
    },
    server: {
      default: false,
      type: Boolean
    },
    delete: {
      default: false,
      type: Boolean
    },
    type: {
      default: null,
      type: String
    },
    communityOnly: {
      default: false,
      type: Boolean
    }
  },
  data() {
    return {
      vimeo: {
        id: null
      }
    }
  },
  async created() {
    if (this.media.file_type === 'vimeo') {
      await this.getVimeoEmbed(this.media.url)
    }
  },
  methods: {
    getYoutubeId,
    getGenericFileType,
    getMediaUrl,
    handleImageClick(e, media) {
      require('basiclightbox/dist/basicLightbox.min.css')
      const basicLightbox = require('basiclightbox')
      basicLightbox
        .create(`<img src="${getMediaUrl(media.media_file, this.isServer)}">`, {
          closable: true
        })
        .show()
    },
    async getVimeoEmbed(link) {
      const result = await this.$axios.$get(
        `https://vimeo.com/api/oembed.json?url=${link}`
      )
      this.vimeo.id = result.video_id
      return result.video_id
    }
  }
}
</script>
<style>
.media-image {
  display: block;
  max-width: 100%;
  width: auto;
  height: auto;
}
</style>
