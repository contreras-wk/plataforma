import useJwt from '@/auth/jwt/useJwt'
// import { useToast } from 'vue-toastification/composition'
// import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'

function studies(dStudies, candidate) {
  const dStudiesOK = dStudies
  dStudiesOK.candidate = candidate
  useJwt.saveCandidateStudies(dStudiesOK)
    .then(response => {
      console.log('Estudios guardado')
      console.log(response)
    })
    .catch(error => {
      console.log(error)
    })
}

function direction(dDirection, candidate) {
  const dDirectionOK = dDirection
  dDirectionOK.candidate = candidate
  useJwt.saveCandidateDirection(dDirectionOK)
    .then(response => {
      console.log('Dirección guardado')
      console.log(response)
    })
    .catch(error => {
      console.log(error)
    })
}

function contatc(dContact, candidate) {
  const dContactOK = dContact
  dContactOK.candidate = candidate
  useJwt.saveCandidateContact(dContactOK)
    .then(response => {
      console.log('Contacto guardado')
      console.log(response)
    })
    .catch(error => {
      console.log(error)
    })
}

function documents(dDocuments, candidate) {
  const dDocumentsOK = dDocuments
  dDocumentsOK.candidate = candidate
  useJwt.saveCandidateDocuments(dDocumentsOK)
    .then(response => {
      console.log('Documentos guardados')
      console.log(response)
    })
    .catch(error => {
      console.log(error)
    })
}

export default function save(dForm, dStudies, dDirection, dContact, dDocuments) {
  useJwt.saveCandidate(dForm)
    .then(response => {
      console.log('Prebecario guardado')
      console.log(response)
      studies(dStudies, response.data.id)
      direction(dDirection, response.data.id)
      contatc(dContact, response.data.id)
      documents(dDocuments, response.data.id)
    })
    .catch(error => {
      console.log(error)
    })
}
