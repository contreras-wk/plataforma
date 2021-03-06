<template>
  <div>
    <!-- color="#7367F0" -->
    <form-wizard
      color="#28a745"
      :title="null"
      :subtitle="null"
      shape="square"
      finish-button-text="Enviar"
      back-button-text="Atras"
      next-button-text="Siguiente"
      class="m-3"
      @on-complete="formSubmitted"
    >

      <!-- Datos Personales -->
      <!-- :before-change="validationFormDataPersonal" -->
      <tab-content
        title="Datos Personales"
        :before-change="validationFormDataPersonal"
      >
        <validation-observer
          ref="dataPersonalRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Datos Personales
              </h5>
              <small class="text-muted">
                Ingresa los datos personales que se te indican a continuación.
              </small>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="CURP"
                label-for="curp"
              >
                <validation-provider
                  #default="{ errors }"
                  name="CURP"
                  rules="curp|required"
                >
                  <b-form-input
                    id="curp"
                    v-model="form.curp"
                    :state="errors.length > 0 ? false:null"
                    placeholder="CURP"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="RFC"
                label-for="rfc"
              >
                <validation-provider
                  #default="{ errors }"
                  name="RFC"
                  rules="rfc|required"
                >
                  <b-form-input
                    id="rfc"
                    v-model="form.rfc"
                    :state="errors.length > 0 ? false:null"
                    placeholder="RFC"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Nombre(s)"
                label-for="name"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Nombre(s)"
                  rules="name|required"
                >
                  <b-form-input
                    id="name"
                    v-model="form.name"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Nombre(s)"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Apellido Paterno"
                label-for="last_name"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Apellido Paterno"
                  rules="name|required"
                >
                  <b-form-input
                    id="last_name"
                    v-model="form.last_name"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Apellido Paterno"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Apellido Materno"
                label-for="mothers_last_name"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Apellido Materno"
                  rules="name|required"
                >
                  <b-form-input
                    id="mothers_last_name"
                    v-model="form.mothers_last_name"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Apelldio Materno"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- okas -->
            <b-col md="4">
              <b-form-group
                label="Edad"
                label-for="age"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Edad"
                  rules="age|required"
                >
                  <b-form-input
                    id="age"
                    v-model="form.age"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Edad"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="4">
              <validation-provider
                #default="{ errors }"
                name="Género"
                rules="required"
              >
                <b-form-group
                  label="Género"
                  label-for="gender"
                  color="#28a745"
                  :state="errors.length > 0 ? false:null"
                >
                  <v-select
                    id="gender"
                    v-model="selc_gender"
                    :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                    :options="optionsGender"
                    :selectable="option => option.value"
                    placeholder="selecciona una opción"
                    value="value"
                    label="text"
                  />
                  <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </b-col>
            <b-col md="4">
              <b-form-group
                label="Estatura"
                label-for="height"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Estatura"
                  rules="height|required"
                >
                  <b-form-input
                    id="height"
                    v-model="form.height"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Estura en [cm], ejemplo 175"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Estudios -->
      <!--  :before-change="validationFormStudies" -->
      <tab-content
        title="Estudios"
      >
        <validation-observer
          ref="infoRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Estudios
              </h5>
              <small class="text-muted">Ingresa los datos sobre el nivel de estudios que se te indican a continuación. </small>
            </b-col>
            <!-- NIVEL DE ESTUDIOS -->
            <b-col md="6">
              <validation-provider
                #default="{ errors }"
                name="Ultimo grado de estudios"
                rules="required"
              >
                <b-form-group
                  label="Último grado de estudios"
                  label-for="studies"
                  :state="errors.length > 0 ? false:null"
                >
                  <v-select
                    id="stuies"
                    v-model="selc_lvl_std"
                    :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                    :options="optionsLevelStudies"
                    :selectable="option => ! option.value.includes('select_value')"
                    label="text"
                  />
                  <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </b-col>

            <!-- TIPO DE ESTUDIOS -->
            <b-col md="6"
              v-if="selc_lvl_std.value === optionsLevelStudies[0].value"
            >
              <validation-provider
                #default="{ errors }"
                name="type-school"
                rules="required"
              >
                <b-form-group
                  label="Tipo de Bachillerato"
                  label-for="type-school"
                  :state="errors.length > 0 ? false:null"
                >
                  <v-select
                    id="type-school"
                    v-model="selc_type_bach"
                    :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                    :options="optionsTypeSchool"
                    :selectable="option => ! option.value.includes('nothing_selected')"
                    label="text"
                  />
                  <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                    {{ errors[0] }}
                  </b-form-invalid-feedback>
                </b-form-group>
              </validation-provider>
            </b-col>

            <!-- DETALLES LICENCIATURA | MAESTRIA | DOCTORADO -->
            <b-col md="6"
              v-if="selc_lvl_std.value !== optionsLevelStudies[0].value && selc_lvl_std.value"
            >
              <b-form-group
                :label="selc_lvl_std.value"
                label-for="details"
              >
                <validation-provider
                  #default="{ errors }"
                  :name="selc_lvl_std.value"
                  rules="required"
                >
                  <b-form-input
                    id="details"
                    v-model="studies.details"
                    :state="errors.length > 0 ? false:null"
                    :placeholder="selc_lvl_std.value + ' en ...'"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Dirección  -->
      <!-- :before-change="validationFormAddress" -->
      <tab-content
        title="Dirección"
      >
        <validation-observer
          ref="addressRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Dirección
              </h5>
              <small class="text-muted">Ingresa los datos sobre tu dirección</small>
            </b-col>
            <!-- BUSQUEDA -->
            <b-col
              cols="12"
              class="mb-2"
            >
              <vue-autosuggest
                v-model="selected"
                :suggestions="filteredOptions"
                :limit="10"
                :get-suggestion-value="getSuggestionValue"
                :input-props="{id:'autosuggest__input',class:'form-control', placeholder:'Calle, Número, Código Postal'}"
                @input="onInputChange"
              >
                <template slot-scope="{suggestion}">
                  <span class="my-suggestion-item">{{ suggestion.item.title }}</span>
                </template>
              </vue-autosuggest>
            </b-col>

            <!-- LUGAR DE RESIDENCIA -->
            <b-col md="6">
              <b-form-group
                label="Lugar de Residencia"
                label-for="place-residence"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Lugar de residencia"
                  rules="name|required"
                >
                  <b-form-input
                    id="place-residence"
                    v-model="direction.place_of_residence"
                    type="text"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Lugar de residencia"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>

            <!-- DELEGACION o MUNICIPIO -->
            <b-col md="6">
              <b-form-group
                label="Delegación o Municipio"
                label-for="delegation"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Delegación o municipio"
                  rules="name|required"
                >
                  <b-form-input
                    id="delegation"
                    v-model="direction.delegation"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Delegación o municipio"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>

            <!-- COLONIA -->
            <b-col md="6">
              <b-form-group
                label="Colonia"
                label-for="suburb"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Colonia"
                  rules="name|required"
                >
                  <b-form-input
                    id="suburb"
                    v-model="direction.suburb"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Colonia"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>

            <!-- CÓDIGO POSTAL -->
            <b-col md="6">
              <b-form-group
                label="Código Postal"
                label-for="postal-code"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Código postal"
                  rules="digits:5|required"
                >
                  <b-form-input
                    id="postal-code"
                    v-model="direction.postal_code"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Código Postal"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>

            <!-- CALLE -->
            <b-col md="6">
              <b-form-group
                label="Calle"
                label-for="street"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Calle"
                  rules="required"
                >
                  <b-form-input
                    id="street"
                    v-model="direction.street"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Calle"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>

          <!-- NUMERO EXTERIOR -->
            <b-col md="3">
              <b-form-group
                label="Numero Exterior"
                label-for="num-out"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Número exterior"
                  rules="required"
                >
                  <b-form-input
                    id="num-out"
                    v-model="direction.num_outdoor"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Num. Exterior"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>

            <!-- NUMERO INTERIOR -->
            <b-col md="3">
              <b-form-group
                label="Numero exterior"
                label-for="num-in"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Número interior"
                >
                  <b-form-input
                    id="num-in"
                    v-model="direction.num_inside"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Num. Interior"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
        <!-- <direction-form /> -->
      </tab-content>

      <!-- Contacto -->
      <!-- :before-change="validationFormSocial" -->
      <tab-content
        title="Forma de Contacto"
      >
        <validation-observer
          ref="socialRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Contacto
              </h5>
              <small class="text-muted">Ingresa tus formas de contatcto</small>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="Teléfono"
                label-for="telephone"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Teléfono"
                  rules="digits:10|required"
                >
                  <b-form-input
                    id="telephone"
                    v-model="contact.telephone"
                    type="number"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Teléfono (Local)"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="Teléfono Celular"
                label-for="mobile-telephone"
              >
                <validation-provider
                  #default="{ errors }"
                  name="mobile-telephone"
                  rules="digits:10|required"
                >
                  <b-form-input
                    id="mobile-telephone"
                    v-model="contact.mobile_telephone"
                    :state="errors.length > 0 ? false:null"
                    type="number"
                    placeholder="Teléfono celular(10 digitos)"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <b-col md="6">
              <b-form-group
                label="Correo Electrónico"
                label-for="email"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Correo electrónico"
                  rules="required|email"
                >
                  <b-form-input
                    id="email"
                    v-model="contact.email"
                    :state="errors.length > 0 ? false:null"
                    placeholder="correo@dominio.com"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Documentos -->
      <!-- :before-change="validationFormDocuments" -->
      <tab-content
        title="Documentos"
      >
        <validation-observer
          ref="documentsRules"
          tag="form"
        >
          <b-row>
            <b-col
              cols="12"
              class="mb-2"
            >
              <h5 class="mb-0">
                Documentos
              </h5>
              <small class="text-muted">Carga tus archivos que se te piden, estos debedn de estar en escaneados y en Formato PDF con un tamaño menor a 5 MB</small>
            </b-col>

            <!-- ARCHIVO CURP -->
            <b-col md="6">
              <b-form-group
                label="CURP"
                label-for="file-curp"
              >
                <validation-provider
                  #default="{ errors }"
                  name="archivo curp"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-curp"
                    v-model="documents.file_curp"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- ARCHIVO RFC -->
            <b-col md="6">
              <b-form-group
                label="RFC"
                label-for="file-rfc"
              >
              <!-- #default="{ errors }" -->
                <validation-provider
                  #default="{ errors }"
                  name="file-rfc"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-rfc"
                    v-model="documents.file_rfc"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- ARCHIVO ACTA DE NACIMIENTO -->
            <b-col md="6">
              <b-form-group
                label="Acta de Nacimiento"
                label-for="file-birth-certificate"
              >
                <validation-provider
                  #default="{ errors }"
                  name="archivo Acta de Nacimiento"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-birth-certificate"
                    v-model="documents.file_birth_certificate"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- ARCHIVO INE -->
            <b-col md="6">
              <b-form-group
                label="INE"
                label-for="file-ine"
              >
                <validation-provider
                  #default="{ errors }"
                  name="INE"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-ine"
                    v-model="documents.file_ine"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- ARCHIVO COMPROBANTE DE DOMICILIO -->
            <b-col md="6">
              <b-form-group
                label="Comprobante de Domicilio"
                label-for="file-proof-address"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Comprobande de Domicilio"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-proof-address"
                    v-model="documents.file_proof_address"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- ARCHIVO COMPROBANTE DE ESTUDIOS -->
            <b-col md="6">
              <b-form-group
                label="Comprobante de Estudios"
                label-for="file-ine"
              >
                <validation-provider
                  #default="{ errors }"
                  name="Comprobande de Estudios"
                  rules="file|required"
                >
                  <b-form-file
                    id="file-proof-studies"
                    v-model="documents.file_proof_studies"
                    accept=".pdf"
                    :state="errors.length > 0 ? false:null"
                    placeholder="Archivo no seleccionado"
                    browse-text="Buscar"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
          </b-row>
        </validation-observer>
      </tab-content>

      <!-- Acerca de la convocatoria -->
      <!-- :before-change="validationFormCallInfo" -->
      <tab-content
        title="Convocatoria"
      >
      <validation-observer
        ref="callInfoRules"
        tag="form"
      >
        <b-row>
          <b-col
            cols="12"
            class="mb-2"
          >
            <h5 class="mb-0">
              Acerca de la convocatoria
            </h5>
            <small class="text-muted">Ingresa los datos acerca de como te enteraste acerca de la convocatoria.</small>
          </b-col>

          <b-col md="6">
            <validation-provider
              #default="{ errors }"
              name="medio"
              rules="required"
            >
              <b-form-group
                label="¿Cual fue el medio por el cual se enteró de la convocatoria?"
                label-for="medium"
                :state="errors.length > 0 ? false:null"
              >
                <v-select
                  id="medium"
                  v-model="call_info.medium"
                  :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                  :options="optionsMediumCallInfo"
                  :selectable="option => ! option.value.includes('select_value')"
                  label="text"
                >
                <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                  {{ errors[0] }}
                </b-form-invalid-feedback>
                </v-select>
              </b-form-group>
            </validation-provider>
          </b-col>
          <!-- v-if="studies.level_of_studies.value !== optionsLevelStudies[0].value && studies.level_of_studies.value" -->
          <b-col md="6"
            v-if="call_info.medium.value === optionsMediumCallInfo[2].value ||
              call_info.medium.value === optionsMediumCallInfo[6].value ||
              call_info.medium.value === optionsMediumCallInfo[7].value ||
              call_info.medium.value === optionsMediumCallInfo[9].value"
          >
              <b-form-group
                :label="'ESPECIFICA ' + call_info.medium.value"
                label-for="call-info-medium"
              >
                <validation-provider
                  #default="{ errors }"
                  :name="call_info.medium.value"
                  rules="required"
                >
                  <b-form-input
                    id="call-info-medium"
                    v-model="call_info.medium_details"
                    :state="errors.length > 0 ? false:null"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
            <!-- ######################################### -->
            <b-col md="6">
            <validation-provider
              #default="{ errors }"
              name="medio"
              rules="required"
            >
              <b-form-group
                label="¿Que fue lo que le atrajo de la convocataria?"
                label-for="attraction"
                :state="errors.length > 0 ? false:null"
              >
                <v-select
                  id="attraction"
                  v-model="call_info.attraction"
                  :dir="$store.state.appConfig.isRTL ? 'rtl' : 'ltr'"
                  :options="optionsAttractionCallInfo"
                  :selectable="option => ! option.value.includes('select_value')"
                  label="text"
                >
                <b-form-invalid-feedback :state="errors.length > 0 ? false:null">
                  {{ errors[0] }}
                </b-form-invalid-feedback>
                </v-select>
              </b-form-group>
            </validation-provider>
          </b-col>
          <!-- v-if="studies.level_of_studies.value !== optionsLevelStudies[0].value && studies.level_of_studies.value" -->
          <b-col md="6"
            v-if="call_info.attraction.value === optionsAttractionCallInfo[3].value"
          >
              <b-form-group
                label="Especifica cual "
                label-for="call-info-medium"
              >
                <validation-provider
                  #default="{ errors }"
                  :name="call_info.medium.value"
                  rules="required"
                >
                  <b-form-input
                    id="call-info-medium"
                    v-model="call_info.attraction_details"
                    :state="errors.length > 0 ? false:null"
                  />
                  <small class="text-danger">{{ errors[0] }}</small>
                </validation-provider>
              </b-form-group>
            </b-col>
        </b-row>
      </validation-observer>
      </tab-content>
    </form-wizard>

  </div>
</template>

<script>
import { VueAutosuggest } from 'vue-autosuggest'
import { FormWizard, TabContent } from 'vue-form-wizard'
import vSelect from 'vue-select'
import { ValidationProvider, ValidationObserver, localize } from 'vee-validate'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
import {
  BRow,
  BCol,
  BFormFile,
  BFormGroup,
  BFormInput,
  BFormInvalidFeedback,
} from 'bootstrap-vue'
import { required, email } from '@validations'
// import SearchDirection from './SearchDirection.vue'
import es from 'vee-validate/dist/locale/es.json'
import axios from 'axios'
// import useJwt from '@/auth/jwt/useJwt'
import save from './save'
import { codeIcon, codeLimiting } from '../code'

localize('es', es)

export default {
  components: {
    // DirectionForm,
    ValidationProvider,
    ValidationObserver,
    FormWizard,
    TabContent,
    BRow,
    BCol,
    BFormFile,
    BFormGroup,
    BFormInput,
    BFormInvalidFeedback,
    vSelect,
    // eslint-disable-next-line vue/no-unused-components
    ToastificationContent,
    VueAutosuggest,
    // SearchDirection,0
  },
  data() {
    return {
      showTypeSchool: false,
      selc_gender: '',
      selc_lvl_std: '',
      selc_type_bach: '',
      form: {
        curp: '',
        rfc: '',
        name: '',
        last_name: '',
        mothers_last_name: '',
        age: '',
        gender: '',
        height: '',
      },
      studies: {
        level_of_studies: '',
        details: '',
      },
      direction: {
        place_of_residence: '',
        delegation: '',
        suburb: '',
        postal_code: '',
        street: '',
        num_outdoor: '',
        num_inside: '',
      },
      contact: {
        telephone: '',
        mobile_telephone: '',
        email: '',
      },
      documents: {
        file_curp: null,
        file_rfc: null,
        file_birth_certificate: null,
        file_ine: null,
        file_proof_address: null,
        file_proof_studies: null,
        file_proof_courses: null,
      },
      call_info: {
        medium: '',
        medium_details: '',
        attraction: '',
        attraction_details: '',
      },
      // VARS FOR AUTOCOMPLETE DIRECTION
      datasuggest: [],
      filteredOptions: [],
      limit: 20,
      selected: '',
      dir: null,
      // #############
      selectedContry: '',
      selectedLanguage: '',
      name: '',
      emailValue: '',
      PasswordValue: '',
      passwordCon: '',
      first_name: '',
      last_name: '',
      address: '',
      landMark: '',
      pincode: '',
      twitterUrl: '',
      facebookUrl: '',
      googleUrl: '',
      linkedinUrl: '',
      city: '',
      required,
      email,
      codeIcon,
      codeLimiting,
      optionsGender: [
        { value: 'F', text: 'Femenino' },
        { value: 'M', text: 'Masculino' },
      ],
      optionsLevelStudies: [
        { value: 'Bachillerato', text: 'Bachillerato' },
        { value: 'Licenciatura', text: 'Licenciatura' },
        { value: 'Maestría', text: 'Maestría' },
        { value: 'Doctorado', text: 'Doctorado' },
      ],
      optionsTypeSchool: [
        { value: 'BACHILLERES', text: 'BACHILLERES' },
        { value: 'CBT', text: 'CBT' },
        { value: 'CBTIS', text: 'CEBETIS' },
        { value: 'CECYT', text: 'CECYT' },
        { value: 'CECYTEM', text: 'CECYTEM' },
        { value: 'CETIS', text: 'CETIS' },
        { value: 'CONALEP', text: 'CONALEP' },
        { value: 'ESC. PARTICULAR', text: 'ESC. PARTICULAR' },
        { value: 'PREPARATORIA DE LA CDMX', text: 'PREPARATORIA DE LA CDMX' },
        { value: 'PREPARTORIA DE LA UNAM', text: 'PREPARTORIA DE LA UNAM' },
        { value: 'PREPARATORIA ESTATAL', text: 'PREPARATORIA ESTATAL' },
        { value: 'SISTEMA ABIERTO', text: 'SISTEMA ABIERTO' },
      ],
      optionsMediumCallInfo: [
        { value: 'AMISTAD O PARIENTE', text: 'AMISTAD O PARIENTE' },
        { value: 'CONOCIDO', text: 'CONOCIDO' },
        { value: 'FERIA DE EMPLEO', text: 'FERIA DE EMPLEO' },
        { value: 'INTERNET', text: 'INTERNET' },
        { value: 'LLAMADA TELÉFONICA', text: 'LLAMADA TELÉFONICA' },
        { value: 'METRO', text: 'METRO' },
        { value: 'OTRO', text: 'OTRO' },
        { value: 'PERIÓDICO', text: 'PERIÓDICO' },
        { value: 'POLICÍA', text: 'POLICÍA' },
        { value: 'SISTEMA NACIONAL DE EMPLEO', text: 'SISTEMA NACIONAL DE EMPLEO' },
        { value: 'TELEVISION', text: 'TELEVISION' },
        { value: 'VOLANTE', text: 'VOLANTE' },
      ],
      optionsAttractionCallInfo: [
        { value: 'DESARROLLO PERSONAL', text: 'DESARROLLO PERSONAL' },
        { value: 'ESTABILIDAD ECONÓMICA', text: 'ESTABILIDAD ECONÓMICA' },
        { value: 'OPORTUNIDAD DE TRABAJO', text: 'OPORTUNIDAD DE TRABAJO' },
        { value: 'OTRA OPCION', text: 'OTRA OPCION' },
        { value: 'POR VOCACIÓN', text: 'POR VOCACIÓN' },
        { value: 'PRESTACIONES', text: 'PRESTACIONES' },
        { value: 'SERVIVIO A MI CIUDAD', text: 'SERVIVIO A MI CIUDAD' },
        { value: 'SUELDO', text: 'SUELDO' },
      ],
    }
  },
  updated() {
  },
  // watch() {
  // },
  methods: {
    formSubmitted() {
      // Datos personales
      this.form.gender = this.selc_gender.value
      // Estudios
      this.studies.level_of_studies = this.selc_lvl_std.value
      if (this.studies.level_of_studies === this.optionsLevelStudies[0].value) {
        this.studies.details = this.selc_type_bach.value
        console.log('Asigno el tipo de bachilleres')
      }
      // Dirección no aignaciones
      if (!this.direction.num_inside) {
        delete this.direction.num_inside
      }
      console.log(this.contact)
      console.log('##############################')
      console.log(this.documents)
      save(
        this.form,
        this.studies,
        this.direction,
        this.contact,
        this.documents,
      )
      // console.log('enviar formulario')
      // this.form.gender = this.selc_gender.value
      // console.log(this.form)
      // useJwt.saveCandidate(this.form)
      //   .then(response => {
      //     console.log(response)
      //     this.$toast({
      //       component: ToastificationContent,
      //       props: {
      //         title: 'Su registro ha sido completado',
      //         icon: 'CheckCircleIcon',
      //         variant: 'success',
      //       },
      //     })
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
    },
    validationFormDataPersonal() {
      return new Promise((resolve, reject) => {
        this.$refs.dataPersonalRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            reject()
          }
        })
      })
    },
    validationFormInfo() {
      return new Promise((resolve, reject) => {
        this.$refs.infoRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            console.log('Algo salio mal')
            reject()
          }
        })
      })
    },
    validationFormAddress() {
      return new Promise((resolve, reject) => {
        this.$refs.addressRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            reject()
          }
        })
      })
    },
    validationFormSocial() {
      return new Promise((resolve, reject) => {
        this.$refs.socialRules.validate().then(success => {
          if (success) {
            resolve(true)
          } else {
            reject()
          }
        })
      })
    },
    // validationFormDocuments() {
    //   return new Preomise((resolve, reject) => {
    //     this.$refs.s
    //   })
    // },
    // ###########################################
    onInputChange(text) {
      console.log(this.dir)
      console.log('########################')
      // console.log('onInputChange')
      if (text === '' || text === undefined) {
        this.filteredOptions = []
        this.selected = ''
        this.dir = null
        this.direction.place_of_residence = ''
        this.direction.delegation = ''
        this.direction.suburb = ''
        this.direction.postal_code = ''
        this.direction.street = ''
        this.direction.num_outdoor = ''
        return
      }
      // GEOCODE
      // const url = `https://geocode.search.hereapi.com/v1/geocode?q=${text}&in=countryCode:MEX&apiKey=WnMOYAfN-NKNdKhRyMWxnXHzg-psiHuRzz576BKAN2g`
      // PLACE
      // const url = `https://places.api.here.com/places/v1/discover/search?at=19.4978,-99.1269&tf=plain&addressFilter=countryCode=MEX&q=${text}&app_id=CPBypQwM5DBlqg0kVMIK&app_code=NXIYJllYjgaayfuimeBPCg`
      // AUTOCOMPLETE
      const url = `https://autocomplete.search.hereapi.com/v1/autocomplete?q=${text}&in=countryCode:MEX&apiKey=WnMOYAfN-NKNdKhRyMWxnXHzg-psiHuRzz576BKAN2g`
      axios.get(url)
        .then(response => {
          if (response.status !== 400) {
            this.datasuggest = response.data.items
            console.log(this.datasuggest)
            this.filteredOptions = [{
              data: this.datasuggest,
            }]
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    getSuggestionValue(suggestion) {
      this.dir = suggestion.item.address
      this.direction.place_of_residence = this.dir.state
      this.direction.delegation = this.dir.city
      this.direction.suburb = this.dir.district
      this.direction.postal_code = this.dir.postalCode
      this.direction.street = this.dir.street
      this.direction.num_outdoor = this.dir.houseNumber
      // this.direction.
      return suggestion.item.title
    },
  },
  created() {

  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/libs/vue-autosuggest.scss';
</style>
