export default {
  // Endpoints
  loginEndpoint: 'token/',
  // Candidate Prebecarios
  candidates: 'prebecarios/',
  candidateUpdate: 'prebecarios/update/',
  candidatesStudies: 'prebecarios/studie/',
  candidatesDirection: 'prebecarios/direction/',
  candidatesContact: 'prebecarios/contact/',
  candidatesDocuments: 'prebecarios/document/',
  // Scholar Becarios
  scholar: 'becarios/',
  // This will be prefixed in authorization header with token
  // e.g. Authorization: Bearer <token>
  tokenType: 'Bearer',
  // Value of this property will be used as key to store JWT token in storage
  storageTokenKeyName: 'accessToken',
  storageRefreshTokenKeyName: 'refreshToken',
}
