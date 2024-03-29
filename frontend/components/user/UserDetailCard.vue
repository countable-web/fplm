<template>
  <div class="user-detail-card">
    <Card>
      <template v-slot:header>
        <div
          class="user-detail-icon-container"
          :style="'background-color:' + color"
        >
          <img src="@/assets/images/language_icon.svg" alt="Language" />
        </div>
      </template>
      <template v-slot:body>
        <div>
          <div>
            <h5
              class="font-07 m-0 p-0 color-gray text-uppercase font-weight-normal"
            >
              User
            </h5>
            <h5 class="font-09 m-0 p-0 color-gray font-weight-bold">
              {{ name }}
            </h5>
          </div>
        </div>
        <div v-if="edit && id" class="d-inline-block">
          <CardBadge
            content="Edit"
            type="edit"
            @click.native="
              $router.push({
                path: `/profile/edit/${id}`
              })
            "
          ></CardBadge>
        </div>
        <div v-if="approval && id" class="d-inline-block">
          <CardBadge
            content="Approval"
            type="edit"
            @click.native="
              $router.push({
                path: `/profile/approvals`
              })
            "
          ></CardBadge>
        </div>
      </template>
      <template v-slot:footer>
        <div
          class="fpcc-card-more"
          @click.prevent="handleReturn"
          @mouseover.prevent="handleMouseOver"
          @mouseleave="handleMouseLeave"
        >
          <img
            v-if="!hover"
            class="ml-1"
            src="@/assets/images/return_icon_hover.svg"
            alt="Go"
          />
          <img
            v-else
            class="ml-1"
            src="@/assets/images/return_icon_hover.svg"
            alt="Go"
          />
          <span class="ml-1 font-weight-bold">Return</span>
        </div>
      </template>
    </Card>
  </div>
</template>

<script>
import Card from '@/components/Card.vue'
import CardBadge from '@/components/CardBadge.vue'
import { encodeFPCC } from '@/plugins/utils.js'

export default {
  components: {
    Card,
    CardBadge
  },
  props: {
    name: {
      type: String,
      default: ''
    },
    color: {
      type: String,
      default: 'RGB(0, 0, 0)'
    },
    detail: {
      type: Boolean,
      default: false
    },
    server: {
      type: Boolean,
      default: false
    },
    audioFile: {
      type: String,
      default: null
    },
    link: {
      type: String,
      default: ''
    },
    edit: {
      type: Boolean,
      default: null
    },
    id: {
      type: Number,
      default: null
    },
    approval: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      hover: false
    }
  },
  computed: {
    comingFromDetail() {
      return this.$store.state.languages.comingFromDetail
    }
  },
  methods: {
    handlePronounce() {
      this.audio = this.audio || new Audio(this.audioFile)
      if (this.audio.paused) {
        this.audio.play()
      } else {
        this.audio.pause()
      }
    },
    handleReturn() {
      if (!this.detail) {
        if (this.server) {
          this.$router.push({ path: '/languages' })
        } else if (this.comingFromDetail) {
          this.$router.push({ path: '/languages' })
          this.$store.commit('languages/setComingFromDetail', false)
        } else {
          this.$router.go(-1)
        }
      } else {
        this.$store.commit('languages/setComingFromDetail', true)
        this.$router.push({
          path: `/languages/${encodeFPCC(this.$route.params.lang)}`
        })
      }
    },
    handleMouseOver() {
      this.hover = true
    },
    handleMouseLeave() {
      this.hover = false
    }
  }
}
</script>

<style scoped>
.user-detail-card {
  cursor: pointer;
}
.user-detail-icon-container {
  background-color: black;
  border-radius: 50%;
  height: 43px;
  width: 43px;
}
.user-detail-icon-container img {
  display: inline-block;
  width: 100%;
  height: 100%;
}
.fpcc-card-more {
  background-color: #c46156;
  display: flex;
  align-items: center;
  height: 35px;
  justify-content: center;
  border-top-left-radius: 0.5em;
  border-bottom-left-radius: 0.5em;
  color: white;
}

.fpcc-card-more {
  padding: 0.3em;
  font-size: 0.7em;
}

.fpcc-card-more:hover {
  color: white;
  background-color: #454545;
}

.fpcc-card-more img {
  display: inline-block;
  width: 15px;
  height: 15px;
}

.fpcc-card {
  border: 0;
  box-shadow: none;
}
</style>
