import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([createUser(), uploadPhoto()])
    .then(([user, response]) => {
      console.log(response.body, user.firstName, user.lastName);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
