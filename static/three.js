import THREE from 'https://cdn.jsdelivr.net/npm/three@0.137.5/build/three.min.js';
import { GLTFLoader } from 'https://unpkg.com/three@0.154.0/examples/jsm/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize( window.innerWidth, window.innerHeight );
renderer.setAnimationLoop( animate );
document.body.appendChild( renderer.domElement );

// Create a cube and add it to the scene
const geometry = new THREE.BoxGeometry();
const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

//chargement d'un modele 3d
const cadenas = new GLTFLoader();

cadenas.load('/static/assets/cadenas.gltf', function (gltf) {
  scene.add(gltf.scene);
}, undefined, function (error) {
  console.error('Error loading truck model:', error);
});

// Position the camera
camera.position.z = 5;

// Render the scene and camera
function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();
