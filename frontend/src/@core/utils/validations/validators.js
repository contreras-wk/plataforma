export const validatorPositive = value => {
  if (value >= 0) {
    return true
  }
  return false
}

export const validatorPassword = password => {
  /* eslint-disable no-useless-escape */
  const regExp = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%&*()]).{8,}/
  /* eslint-enable no-useless-escape */
  const validPassword = regExp.test(password)
  return validPassword
}

export const validatorCreditCard = creditnum => {
  /* eslint-disable no-useless-escape */
  const cRegExp = /^(?:3[47][0-9]{13})$/
  /* eslint-enable no-useless-escape */
  const validCreditCard = cRegExp.test(creditnum)
  return validCreditCard
}

export const validatorUrlValidator = val => {
  if (val === undefined || val === null || val.length === 0) {
    return true
  }
  /* eslint-disable no-useless-escape */
  const re = /^(http[s]?:\/\/){0,1}(www\.){0,1}[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,5}[\.]{0,1}/
  /* eslint-enable no-useless-escape */
  return re.test(val)
}

export const validatorCURP = curp => {
  if (curp.length === 18) {
    const cRegExp = /([A-Za-z0-9])$/
    return cRegExp.test(curp)
  }
  return false
}

export const validatorRFC = rfc => {
  if (rfc.length === 13) {
    const cRegExp = /([A-Za-z0-9])$/
    return cRegExp.test(rfc)
  }
  return false
}

export const validatorNames = name => {
  const re = /([A-Za-z])$/
  return re.test(name)
}

export const validatorAge = age => {
  const re = /([0-9])$/
  if (re.test(age) && age >= 18 && age <= 40) {
    return true
  }
  return false
}

export const validatorHeight = height => {
  const re = /([0-9])$/
  if (re.test(height) && height >= 150 && height <= 250) {
    return true
  }
  return false
}

export const validatorFilePFD = file => {
  // 1 MB = 1048576 bytes
  // Size to file is five Megabytes
  const SIZE_FILE = 5242880
  const TYPE_FILE = 'application/pdf'
  return file.size <= SIZE_FILE && file.type === TYPE_FILE
}
