<template>
  <div class="d-inline-block">
    <b-badge
      class="badge"
      :style="'background-color: ' + bgcolor"
      :class="'badge-' + mode"
      @click="handleClick"
    >
      <span class="badge-icon">
        <img :src="getImage" alt="Icon" />
      </span>
      <span class="badge-content">{{ content }}</span>
      <span class="badge-number">{{ number }}</span>
    </b-badge>

    <b-modal v-model="showModal" hide-header @ok="handleOk">
      <h5>Additional Criteria</h5>
      <b-form-checkbox
        v-for="option in categories"
        :key="option.id"
        v-model="selected"
        :value="option.id"
      >
        {{ option.name }}
      </b-form-checkbox>
    </b-modal>
  </div>
</template>

<script>
import { getApiUrl } from '@/plugins/utils.js'

export default {
  props: {
    content: {
      type: String,
      default: ''
    },
    number: {
      type: Number,
      default: 0
    },
    bgcolor: {
      type: String,
      default: '#707070'
    },
    image: {
      type: String,
      default: 'language_icon_white.svg'
    },
    type: {
      type: String,
      default: ''
    },
    mode: {
      type: String,
      default: 'neutral'
    },
    places: {
      type: Array,
      default() {
        return []
      }
    }
  },
  data() {
    return {
      showModal: false,
      categories: [],
      selected: this.$store.state.places.filterCategories
    }
  },
  computed: {
    badgePlaces() {
      return this.$store.state.places.badgePlaces
    },
    getImage() {
      return {
        language: '/language_icon_white.svg',
        community: '/community_icon_white.svg',
        org: '/organization_icon_white.svg',
        event: '/event_icon_white.svg',
        part: '/public_art_icon_white.svg',
        poi: '/poi_icon_white.svg'
      }[this.type]
    }
  },
  methods: {
    async handleClick() {
      if (this.type !== 'poi') return false

      if (this.mode === 'active') {
        this.$store.commit('places/setFilteredBadgePlaces', this.badgePlaces)
        return false
      }
      const url = getApiUrl('placenamecategory/')

      if (this.categories.length === 0) {
        const result = await this.$axios.$get(url)
        this.categories = result
      }

      this.showModal = true
    },

    handleOk(e) {
      e.preventDefault()
      if (this.selected.length === 0) {
        this.$store.commit('places/setFilteredBadgePlaces', this.badgePlaces)
        this.$store.commit('places/setFilterCategories', this.selected)
        this.$root.$emit('updatePlacesCategory', this.selected)
      } else {
        this.$store.commit('places/setFilterCategories', this.selected)
        this.$root.$emit('updatePlacesCategory', this.selected)

        this.$store.commit(
          'places/setFilteredBadgePlaces',
          this.badgePlaces.filter(bp => {
            return this.selected.find(s => s === bp.category)
          })
        )
      }

      this.showModal = false

      console.log('Ok!')
    }
  }
}
</script>

<style>
.badge {
  border-radius: 1em;
}
.badge-content {
  display: inline-block;
  margin: 0 0.25em;
  font-size: 1em;
}
.badge-number {
  display: inline-block;
  color: #c46257;
  background-color: white;
  height: 19px;
  width: 19px;
  text-align: center;
  border-radius: 50%;
  font-size: 0.8em;
  line-height: 19px;
}
.badge-icon {
  display: inline-block;
}
.badge-icon img {
  display: inline-block;
  width: 19px;
}

.badge-inactive {
  opacity: 0.5;
}

.badge-active {
  opacity: 1;
  box-shadow: 0px 1px 4px 2px rgba(0, 0, 0, 0.3);
}

@media (max-width: 992px) {
  .badge-icon {
    display: none;
  }

  .badge-content {
    display: inline-block;
    font-size: 0.8em;
  }
  .badge-number {
    font-size: 0.8em;
  }
}

@media (max-width: 574px) {
  .badge-icon {
    display: inline-block;
  }

  .badge-content {
    display: none;
  }
}
</style>
