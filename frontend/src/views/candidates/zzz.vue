<template>
  <b-col md="6">
    <b-form-group
      label="Telefono"
      label-for="telephone"
    >
      <validation-provider
        #default="{ errors }"
        name="telephone"
        rules="digits:10|required"
      >
        <b-form-input
          id="telephone"
          v-model="twitterUrl"
          type="number"
          :state="errors.length > 0 ? false:null"
          placeholder=""
        />
        <small class="text-danger">{{ errors[0] }}</small>
      </validation-provider>
    </b-form-group>
  </b-col>

</template>

<script>
export default {

}
</script>

<style>

</style>
