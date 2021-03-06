export default {
  // Endpoints
  loginEndpoint: 'token/',
  // LIST AND CREATE CANDIDATES
  candidates: 'prebecarios/',
  candidatesStudies: 'prebecarios/studie/',
  candidatesDirection: 'prebecarios/direction/',
  candidatesContact: 'prebecarios/contact/',
  candidatesDocuments: 'prebecarios/document/',
  // This will be prefixed in authorization header with token
  // e.g. Authorization: Bearer <token>
  tokenType: 'Bearer',
  // Value of this property will be used as key to store JWT token in storage
  storageTokenKeyName: 'accessToken',
  storageRefreshTokenKeyName: 'refreshToken',
}
